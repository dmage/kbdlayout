#!/usr/bin/env python
# -*- coding: utf-8 -*-

class RenderContext:
    def __init__(self, x, y, *, scale, keymap=None):
        self.x = x
        self.y = y
        self.scale = scale
        self.m = 1
        self.keymap = keymap

    def shift(self, dx, dy):
        return RenderContext(self.x+dx, self.y+dy, scale=self.scale, keymap=self.keymap)

    def label(self, keycode):
        if not isinstance(keycode, int):
            return keycode
        return self.keymap.get(keycode, "")


def xml_escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def svg_label(text_x, label):
    if ' ' in label:
        words = label.split(' ')
        return f'<tspan x="{text_x}" dy="0">{xml_escape(words[0])}</tspan>' + ''.join(f'<tspan x="{text_x}" dy="1em">{xml_escape(word)}</tspan>' for word in words[1:])
    return xml_escape(label)


class Key:
    def __init__(self, label, *, width=1, height=1):
        self._label = label
        self._width = width
        self._height = height

    def __repr__(self):
        args = [repr(self._label)]
        if self._width != 1:
            args.append(f'width={self._width}')
        if self._height != 1:
            args.append(f'height={self._height}')
        return f'Key({", ".join(args)})'

    def render(self, ctx):
        label = ctx.label(self._label)
        width = self._width*ctx.scale
        height = self._height*ctx.scale
        text_x = ctx.x + width/2
        text_y = ctx.y + height/2
        return (
            f'<rect x="{ctx.x + ctx.m}" y="{ctx.y + ctx.m}" width="{width - 2*ctx.m}" height="{height - 2*ctx.m}"/>',
            f'<text x="{text_x}" y="{text_y}">{svg_label(text_x, label)}</text>',
            width, height,
        )


class ISOEnterKey:
    def __init__(self, label, width1, width2, height1, height2):
        self._label = label
        self._width1 = width1
        self._width2 = width2
        self._height1 = height1
        self._height2 = height2

    def __repr__(self):
        return f'ISOEnterKey({self._label}, {self._width1}, {self._width2}, {self._height1}, {self._height2})'

    def _points(self, p_deltas, margin):
        p, deltas = p_deltas[0], p_deltas[1:]
        s = f'{p[0] + margin[0][0]},{p[1] + margin[0][1]}'
        for ((dx, dy), (mx, my)) in zip(deltas, margin[1:]):
            p = (p[0]+dx, p[1]+dy)
            s += f' {p[0] + mx},{p[1] + my}'
        return s

    def render(self, ctx):
        label = ctx.label(self._label)
        width1 = self._width1*ctx.scale
        width2 = self._width2*ctx.scale
        height1 = self._height1*ctx.scale
        height2 = self._height2*ctx.scale
        p = self._points(
            [(ctx.x, ctx.y), (width1, 0), (0, height1+height2), (-width2, 0), (0, -height2), (-width1+width2, 0), (0, -height1)],
            [(ctx.m, ctx.m), (-ctx.m, ctx.m), (-ctx.m, -ctx.m), (ctx.m, -ctx.m), (ctx.m, -ctx.m), (ctx.m, -ctx.m), (ctx.m, ctx.m)],
        )
        return (
            f'<polygon points="{p}"/>',
            f'<text x="{ctx.x + width1/2}" y="{ctx.y + height1/2}">{svg_label(ctx.x + width1/2, label)}</text>',
            width1+width2, height1+height2,
        ) 


class Space:
    def __init__(self, width=1, *, height=1):
        self._width = width
        self._height = height

    def __repr__(self):
        args = []
        if self._width != 1:
            args.append(f'width={self._width}')
        if self._height != 1:
            args.append(f'height={self._height}')
        return f'Space({", ".join(args)})'

    def render(self, ctx):
        return (f'', f'', self._width*ctx.scale, self._height*ctx.scale)


class Row:
    def __init__(self, children):
        self._children = children

    def __repr__(self):
        return f'Row({", ".join(repr(child) for child in self._children)})'

    def render(self, ctx):
        svg_rects, svg_texts, width, height = self._children[0].render(ctx)
        total_width = width
        for child in self._children[1:]:
            child_svg_rects, child_svg_texts, child_width, child_height = child.render(ctx.shift(width, 0))
            if child_height != height:
                raise ValueError('Children have different heights: {} (height: {}) and {} (height: {})'.format(self._children[0], height, child, child_height))
            svg_rects += child_svg_rects
            svg_texts += child_svg_texts
            total_width += child_width
            ctx = ctx.shift(child_width, 0)
        return svg_rects, svg_texts, total_width, height


class TwoRowsISOEnter:
    def __init__(self, row1, row2, label, width1, width2):
        self._row1 = row1
        self._row2 = row2
        self._label = label
        self._width1 = width1
        self._width2 = width2

    def __repr__(self):
        return f'TwoRowsISOEnter({self._row1}, {self._row2}, {self._width1}, {self._width2})'

    def render(self, ctx):
        row1_svg_rects, row1_svg_texts, row1_width, row1_height = self._row1.render(ctx)
        row2_svg_rects, row2_svg_texts, row2_width, row2_height = self._row2.render(ctx.shift(0, row1_height))
        total_row1_width = row1_width + self._width1*ctx.scale
        total_row2_width = row2_width + self._width2*ctx.scale
        if total_row1_width != total_row2_width:
            raise ValueError('Rows have different widths: {}+{} (width: {}) and {}+{} (width: {})'.format(row1_width, self._width1*ctx.scale, total_row1_width, row2_width, self._width2*ctx.scale, total_row2_width))
        enter_key = ISOEnterKey(self._label, self._width1, self._width2, row1_height/ctx.scale, row2_height/ctx.scale)
        enter_svg_rects, enter_svg_texts, enter_width, enter_height = enter_key.render(ctx.shift(row1_width, 0))
        return (
            row1_svg_rects + row2_svg_rects + enter_svg_rects,
            row1_svg_texts + row2_svg_texts + enter_svg_texts,
            total_row1_width,
            row1_height + row2_height,
        )


class TwoRowsKey:
    def __init__(self, row1, row2, label):
        self._row1 = row1
        self._row2 = row2
        self._label = label

    def __repr__(self):
        return f'TwoRowsKey({self._row1}, {self._row2}, {self._label})'

    def render(self, ctx):
        row1_svg_rects, row1_svg_texts, row1_width, row1_height = self._row1.render(ctx)
        row2_svg_rects, row2_svg_texts, row2_width, row2_height = self._row2.render(ctx.shift(0, row1_height))
        if row1_width != row2_width:
            raise ValueError('Rows have different widths: {} (width: {}) and {} (width: {})'.format(self._row1, row1_width, self._row2, row2_width))
        key_svg_rects, key_svg_texts, key_width, key_height = Key(self._label, height=(row1_height+row2_height)/ctx.scale).render(ctx.shift(row1_width, 0))
        return (
            row1_svg_rects + row2_svg_rects + key_svg_rects,
            row1_svg_texts + row2_svg_texts + key_svg_texts,
            row1_width + key_width,
            row1_height + row2_height,
        )


class VBlock:
    def __init__(self, children):
        self._children = children

    def __repr__(self):
        return f'VBlock({", ".join(repr(child) for child in self._children)})'

    def render(self, ctx):
        svg_rects, svg_texts, width, height = self._children[0].render(ctx)
        total_height = height
        for child in self._children[1:]:
            child_svg_rects, child_svg_texts, child_width, child_height = child.render(ctx.shift(0, height))
            if child_width != width:
                raise ValueError('Children have different widths: {} (width: {}) and {} (width: {})'.format(self._children[0], width, child, child_width))
            svg_rects += child_svg_rects
            svg_texts += child_svg_texts
            total_height += child_height
            ctx = ctx.shift(0, child_height)
        return svg_rects, svg_texts, width, total_height


class HBlock:
    def __init__(self, *children):
        self._children = children

    def __repr__(self):
        return f'HBlock({", ".join(repr(child) for child in self._children)})'

    def render(self, ctx):
        svg_rects, svg_texts, width, height = self._children[0].render(ctx)
        total_width = width
        for child in self._children[1:]:
            child_svg_rects, child_svg_texts, child_width, child_height = child.render(ctx.shift(width, 0))
            if child_height != height:
                raise ValueError('Children have different heights: {} (height: {}) and {} (height: {})'.format(self._children[0], height, child, child_height))
            svg_rects += child_svg_rects
            svg_texts += child_svg_texts
            total_width += child_width
            ctx = ctx.shift(child_width, 0)
        return svg_rects, svg_texts, total_width, height

# from https://github.com/legionus/kbd/blob/master/src/libkeymap/syms.synonyms.h
keysym_synonyms = {
    "Control_h": "BackSpace",
	"Control_i": "Tab",
	"Control_j": "Linefeed",
	"Home": "Find",
	"End": "Select",
	"PageUp": "Prior",
	"PageDown": "Next",
	"multiplication": "multiply",
	"pound": "sterling",
	"pilcrow": "paragraph",
	"Oslash": "Ooblique",
	"Shift_L": "ShiftL",
	"Shift_R": "ShiftR",
	"Control_L": "CtrlL",
	"Control_R": "CtrlR",
	"AltL": "Alt",
	"AltR": "AltGr",
	"Alt_L": "Alt",
	"Alt_R": "AltGr",
	"AltGr_L": "Alt",
	"AltGr_R": "AltGr",
	"AltLLock": "Alt_Lock",
	"AltRLock": "AltGr_Lock",
	"SCtrl": "SControl",
	"Spawn_Console": "KeyboardSignal",
	"Uncaps_Shift": "CapsShift",
	"lambda": "lamda",
	"Lambda": "Lamda",
	"xi": "ksi",
	"Xi": "Ksi",
	"chi": "khi",
	"Chi": "Khi",
	"tilde": "asciitilde",
	"circumflex": "asciicircum",
	"dead_ogonek": "dead_cedilla",
	"dead_caron": "dead_circumflex",
	"dead_breve": "dead_tilde",
	"dead_doubleacute": "dead_tilde",
	"Idotabove": "Iabovedot",
	"dotlessi": "idotless",
	"no-break_space": "nobreakspace",
	"paragraph_sign": "section",
	"soft_hyphen": "hyphen",
	"bielorussian_cyrillic_capital_letter_i": "ukrainian_cyrillic_capital_letter_i",
	"cyrillic_capital_letter_kha": "cyrillic_capital_letter_ha",
	"cyrillic_capital_letter_ge": "cyrillic_capital_letter_ghe",
	"cyrillic_capital_letter_ia": "cyrillic_capital_letter_ya",
	"cyrillic_capital_letter_iu": "cyrillic_capital_letter_yu",
	"cyrillic_capital_letter_yeri": "cyrillic_capital_letter_yeru",
	"cyrillic_capital_letter_reversed_e": "cyrillic_capital_letter_e",
	"cyrillic_capital_letter_ii": "cyrillic_capital_letter_i",
	"cyrillic_capital_letter_short_ii": "cyrillic_capital_letter_short_i",
	"bielorussian_cyrillic_small_letter_i": "ukrainian_cyrillic_small_letter_i",
	"cyrillic_small_letter_kha": "cyrillic_small_letter_ha",
	"cyrillic_small_letter_ge": "cyrillic_small_letter_ghe",
	"cyrillic_small_letter_ia": "cyrillic_small_letter_ya",
	"cyrillic_small_letter_iu": "cyrillic_small_letter_yu",
	"cyrillic_small_letter_yeri": "cyrillic_small_letter_yeru",
	"cyrillic_small_letter_reversed_e": "cyrillic_small_letter_e",
	"cyrillic_small_letter_ii": "cyrillic_small_letter_i",
	"cyrillic_small_letter_short_ii": "cyrillic_small_letter_short_i",
	"ukrainian_cyrillic_small_letter_ghe_with_upturn": "cyrillic_small_letter_ghe_with_upturn",
	"ukrainian_cyrillic_capital_letter_ghe_with_upturn": "cyrillic_capital_letter_ghe_with_upturn",
	"rightanglequote": "guillemotright",
}

def load_keymap(filename, *, keymap=None):
    names = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0',

        'Aacute': 'Á',
        'Ccaron': 'Č',
        'Eacute': 'É',
        'Ecaron': 'Ě',
        'Iacute': 'Í',
        'Rcaron': 'Ř',
        'Scaron': 'Š',
        'Uacute': 'Ú',
        'Uring': 'Ů',
        'Yacute': 'Ý',
        'Zcaron': 'Ž',
        'aacute': 'á',
        'ccaron': 'č',
        'eacute': 'é',
        'ecaron': 'ě',
        'rcaron': 'ř',
        'scaron': 'š',
        'uacute': 'ú',
        'uring': 'ů',
        'yacute': 'ý',
        'zcaron': 'ž',

        'Alt': 'ALT',
        'AltGr': 'ALTGR',
        'Break': 'BREAK',
        'Caps_Lock': 'CAPS LOCK',
        'Control': 'CTRL',
        'Delete': 'BACKSPACE',
        'Down': '↓',
        'Select': 'END',
        'Escape': 'ESC',
        'Find': 'HOME',
        'Insert': 'INS',
        'KP_Add': '+ (KP)',
        'KP_Divide': '/ (KP)',
        'KP_Enter': 'Enter (KP)',
        'KP_Multiply': '* (KP)',
        'KP_Period': '. (KP)',
        'KP_Subtract': '- (KP)',
        'Left': '←',
        'Num_Lock': 'NUM LOCK',
        'Next': 'PGDN',
        'Prior': 'PGUP',
        'Remove': 'DEL',
        'Return': '↵',
        'Right': '→',
        'Scroll_Lock': 'SCROLL LOCK',
        'Shift': 'SHIFT',
        'Tab': 'TAB',
        'Up': '↑',
        'VoidSymbol': 'VOID',
        'ampersand': '&',
        'apostrophe': "'",
        'asciicircum': '^',
        'asciitilde': '~',
        'asterisk': '*',
        'at': '@',
        'backslash': '\\',
        'bar': '|',
        'braceleft': '{',
        'braceright': '}',
        'bracketleft': '[',
        'bracketright': ']',
        'colon': ':',
        'comma': ',',
        'dead_acute': '◌́',
        'dead_caron': '◌̌',
        'dead_diaeresis': '◌̈',
        'dollar': '$',
        'equal': '=',
        'exclam': '!',
        'grave': '`',
        'greater': '>',
        'iacute': 'í',
        'less': '<',
        'minus': '-',
        'numbersign': '#',
        'parenleft': '(',
        'parenright': ')',
        'percent': '%',
        'period': '.',
        'plus': '+',
        'question': '?',
        'quotedbl': '"',
        'section': '§',
        'semicolon': ';',
        'slash': '/',
        'space': 'SPACE',
        'sterling': '£',
        'underscore': '_',
    }
    for i in range(10):
        names[f'KP_{i}'] = f'{i} (KP)'

    modifiers = {
        'plain': 0,
        'shift': 1,
        'altgr': 2,
        'control': 4,
        'alt': 8,
        'shiftl': 16,
        'shiftr': 32,
        'ctrll': 64,
        'ctrlr': 128,
        'capsshift': 256,
    }

    def starts_with_modifier(s):
        for modifier, value in modifiers.items():
            if s.startswith(modifier):
                return True
        return False

    if keymap is None:
        keymap = {}
    with open(filename, 'r', encoding='latin1') as f:
        line_continuation = ''
        for line in f:
            line = line.strip('\n')
            if line.endswith('\\'):
                line_continuation += line[:-1]
                continue
            line = line_continuation + line
            line_continuation = ''

            line = line.split('#', 1)[0].strip()
            if not line:
                continue
            if line.startswith('include'):
                filename = line[len('include'):].strip()
                filename = filename[1:-1] if filename[0] in '\'"' and filename[-1] == filename[0] else filename
                load_keymap('keymaps/' + filename + '.inc', keymap=keymap)
            elif line.startswith('keycode'):
                line = line[len('keycode'):]
                code, definition = line.split('=')
                code = int(code.strip())
                definition = definition.strip().split()
                if not definition:
                    continue
                keysym = definition[0]
                if keysym.startswith('+'):
                    keysym = keysym[1:]
                if keysym in keysym_synonyms:
                    keysym = keysym_synonyms[keysym]
                keymap[code] = names.get(keysym, keysym)
            elif starts_with_modifier(line):
                pass
            elif line.startswith('charset') or line.startswith('keymaps') or line.startswith('alt_is_meta') or line.startswith('string') or line.startswith('compose'):
                pass
            else:
                raise ValueError(f'Unexpected line: {line}')
    return keymap


# TODO
# 84? (Last_Console)
# 85?
# 89, ..., 95?
# 112? (Macro)
# 113? (F13)
# 114? (F14)
# 115? (Help)
# 116? (Do)
# 117? (F17)
# 118? (KP_MinPlus)
# 119? (Pause)
# 120, ..., 124?
# 125? (Decr_Console)
# 126? (Incr_Console)
# 127? (Compose)

# Modifier keys
# Shift 1
# AltGr 2
# Control 4
# Alt 8
# ShiftL 16
# ShiftR 32
# CtrlL 64
# CtrlR 128
# CapsShift 256 

ESC = [Key(1)]
F1_F4 = [Key(i) for i in range(59, 63)]  # F1, F2, F3, F4
F5_F8 = [Key(i) for i in range(63, 67)]  # F5, F6, F7, F8
F9_F12 = [Key(67), Key(68), Key(87), Key(88)]  # F9, F10, F11, F12
ONE_EQUAL = [Key(i) for i in range(2, 14)]  # 1, 2, ..., 0, -, =
Q_P_2 = [Key(i) for i in range(16, 28)]  # Q, W, ..., P, [, ]
A_L_2 = [Key(i) for i in range(30, 41)]  # A, S, ..., L, ;, '
Z_M_3 = [Key(i) for i in range(44, 54)]  # Z, X, ..., M, comma, ., /
PRTSC_BREAK = [Key(99), Key(70), Key(101)]  # Print Screen, Scroll Lock, Break

KEYPAD = [
    Row([Key(69), Key(98), Key(55), Key(74)]),  # Num Lock, KP_Divide, KP_Multiply, KP_Subtract
    TwoRowsKey(
        Row([Key(71), Key(72), Key(73)]),  # KP_7, KP_8, KP_9
        Row([Key(75), Key(76), Key(77)]),  # KP_4, KP_5, KP_6
        78,  # KP_Add
    ),
    TwoRowsKey(
        Row([Key(79), Key(80), Key(81)]),  # KP_1, KP_2, KP_3
        Row([Key(82, width=2), Key(83)]),  # KP_0, KP_Decimal
        96,  # KP_Enter
    ),
]

iso_layout = HBlock(
    VBlock([
        Row(ESC + [Space(1)] + F1_F4 + [Space(0.5)] + F5_F8 + [Space(0.5)] + F9_F12), 
        Space(height=0.5, width=15),
        Row([Key(41)] + ONE_EQUAL + [Key(14, width=2)]),
        TwoRowsISOEnter(
            Row([Key(15, width=1.5)] + Q_P_2),
            Row([Key(58, width=1.75)] + A_L_2 + [Key(43)]),
            28, 1.5, 1.25
        ),
        Row([Key(42, width=1.25), Key(86)] + Z_M_3 + [Key(54, width=2.75)]),
        Row([
            Key(29, width=1.25), Key('?WIN', width=1.25), Key(56, width=1.25),
            Key(57, width=6.25),
            Key(100, width=1.25), Key('?WIN', width=1.25), Key('?MENU', width=1.25), Key(97, width=1.25),
        ]),
    ]),
    Space(0.25, height=6.5),
    VBlock([
        Row(PRTSC_BREAK),
        Space(height=0.5, width=3),
        Row([Key(110), Key(102), Key(104)]),  # Insert, Home, Page Up
        Row([Key(111), Key(107), Key(109)]),  # Remove, End, Page Down
        Space(height=1, width=3),
        Row([Space(1), Key(103), Space(1)]),  # Up
        Row([Key(105), Key(108), Key(106)]),  # Left, Down, Right
    ]),
    Space(0.25, height=6.5),
    VBlock([Space(height=1.5, width=4)] + KEYPAD),
)

import sys
scale = 60
svg_rects, svg_texts, width, height = iso_layout.render(RenderContext(0, 0, scale=scale, keymap=load_keymap(sys.argv[1])))
print(f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="{width+3}" height="{height+3}" viewBox="-1 -1 {width+2} {height+2}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g font-family="Arial" font-size="{scale // 4}px" font-size-adjust="0.518"><g fill="#eee" stroke="#ccc" stroke-linejoin="round">''' + svg_rects + '''</g>
<g fill="#333" text-anchor="middle" text-align="center">''' + svg_texts + '''</g></g>
</svg>''')
