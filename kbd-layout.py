#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

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

KT_LATIN = {
    'nul': '␀',
    'Control_a': 'C-a',
    'Control_b': 'C-b',
    'Control_c': 'C-c',
    'Control_d': 'C-d',
    'Control_e': 'C-e',
    'Control_f': 'C-f',
    'Control_g': 'C-g',
    'BackSpace': 'BS',  # C-h
    'Tab': 'TAB',  # C-i
    'Linefeed': 'LF',  # C-j
    'Control_k': 'C-k',
    'Control_l': 'C-l',
    'Control_m': 'C-m',
    'Control_n': 'C-n',
    'Control_o': 'C-o',
    'Control_p': 'C-p',
    'Control_q': 'C-q',
    'Control_r': 'C-r',
    'Control_s': 'C-s',
    'Control_t': 'C-t',
    'Control_u': 'C-u',
    'Control_v': 'C-v',
    'Control_w': 'C-w',
    'Control_x': 'C-x',
    'Control_y': 'C-y',
    'Control_z': 'C-z',
    'Escape': 'ESC',
    'Control_backslash': 'C-\\',
    'Control_bracketright': 'C-]',
    'Control_asciicircum': 'C-^',
    'Control_underscore': 'C-_',
    'space': 'SPACE',
    'exclam': '!',
    'quotedbl': '"',
    'numbersign': '#',
    'dollar': '$',
    'percent': '%',
    'ampersand': '&',
    'apostrophe': "'",
    'parenleft': '(',
    'parenright': ')',
    'asterisk': '*',
    'plus': '+',
    'comma': ',',
    'minus': '-',
    'period': '.',
    'slash': '/',
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'colon': ':',
    'semicolon': ';',
    'less': '<',
    'equal': '=',
    'greater': '>',
    'question': '?',
    'at': '@',
    # A..Z
    'bracketleft': '[',
    'backslash': '\\',
    'bracketright': ']',
    'asciicircum': '^',
    'underscore': '_',
    'grave': '`',
    # a..z
    'braceleft': '{',
    'bar': '|',
    'braceright': '}',
    'asciitilde': '~',
    'Delete': '⌫',
}
for i in range(26):
    KT_LATIN[chr(ord('a') + i)] = chr(ord("a") + i)
    KT_LATIN[chr(ord('A') + i)] = chr(ord("A") + i)

LABELS = {
    **KT_LATIN,
    'Aacute': 'Á',
    'Ccaron': 'Č',
    'Dstroke': 'Đ',
    'Eacute': 'É',
    'Ecaron': 'Ě',
    'Iacute': 'Í',
    'Lstroke': 'Ł',
    'Rcaron': 'Ř',
    'Scaron': 'Š',
    'Uacute': 'Ú',
    'Uring': 'Ů',
    'Yacute': 'Ý',
    'Zcaron': 'Ž',
    'aacute': 'á',
    'ccaron': 'č',
    'dstroke': 'đ',
    'eacute': 'é',
    'ecaron': 'ě',
    'lstroke': 'ł',
    'rcaron': 'ř',
    'scaron': 'š',
    'ssharp': 'ß',
    'uacute': 'ú',
    'uring': 'ů',
    'yacute': 'ý',
    'zcaron': 'ž',

    'Alt': 'ALT',
    'AltGr': 'ALTGR',
    'AltGr_Lock': 'ALTGR LOCK',
    'Bare_Num_Lock': 'BARE NUM LOCK',
    'Break': 'BREAK',
    'Caps_Lock': 'CAPS LOCK',
    'Compose': 'COM- POSE',
    'Control': 'CTRL',
    'Decr_Console': 'DEC CON',
    'Down': '↓',
    'Escape': 'ESC',
    'Find': 'HOME',
    'Incr_Console': 'INC CON',
    'Insert': 'INS',
    'KP_Add': '+ (KP)',
    'KP_Divide': '/ (KP)',
    'KP_Enter': 'Enter (KP)',
    'KP_Multiply': '* (KP)',
    'KP_Period': '. (KP)',
    'KP_Subtract': '- (KP)',
    'Last_Console': 'LAST CON',
    'Left': '←',
    'Next': 'PGDN',
    'Num_Lock': 'NUM LOCK',
    'Pause': 'PAUSE',
    'Prior': 'PGUP',
    'Remove': 'DEL',
    'Return': '↵',
    'Right': '→',
    'Scroll_Backward': 'SCROLL BACK',
    'Scroll_Forward': 'SCROLL FWD',
    'Scroll_Lock': 'SCROLL LOCK',
    'Select': 'END',
    'Shift': 'SHIFT',
    'ShiftL': 'SHIFTL',
    'ShiftL_Lock': 'SHIFTL LOCK',
    'ShiftR': 'SHIFTR',
    'ShiftR_Lock': 'SHIFTR LOCK',
    'Show_Memory': 'SHOW MEM',
    'Show_Registers': 'SHOW REGS',
    'Show_State': 'SHOW STATE',
    'Tab': 'TAB',
    'Up': '↑',
    'VoidSymbol': '',
    'currency': '¤',
    'dead_acute': '◌́',
    'dead_caron': '◌̌',
    'dead_cedilla': '◌̧',
    'dead_circumflex': '◌̂',
    'dead_diaeresis': '◌̈',
    'dead_grave': '◌̀',
    'dead_tilde': '◌̃',
    'degree': '°',
    'division': '÷',
    'iacute': 'í',
    'multiply': '×',
    'section': '§',
    'sterling': '£',
}
for i in range(10):
    LABELS[f'KP_{i}'] = f'{i} (KP)'
for i in range(64):
    LABELS[f'Console_{i}'] = f'CON{i}'
for keysym, label in KT_LATIN.items():
    LABELS[f'Meta_{keysym}'] = f'M-{label}'


def keysym_label(keysym):
    prefix = ""
    if keysym.startswith('+'):
        prefix = '+'
        keysym = keysym[1:]
    if keysym.startswith('U+'):
        return prefix + chr(int(keysym[2:], 16))
    if keysym in keysym_synonyms:
        keysym = keysym_synonyms[keysym]
    if keysym.startswith('Meta_'):
        non_meta_keysym = keysym[len('Meta_'):]
        if non_meta_keysym in keysym_synonyms:
            non_meta_keysym = keysym_synonyms[non_meta_keysym]
        if non_meta_keysym in KT_LATIN:
            return prefix + 'M-' + KT_LATIN[non_meta_keysym]
        raise ValueError(f'Unknown keysym: {keysym}')
    return prefix + LABELS.get(keysym, keysym)


def main_label(labels):
    if not labels:
        return ""
    label = labels[0]
    if len(label) > 1 and label[0] == '+':
        return label[1:]
    return label


def key_classes(main_label):
    if main_label == 'CAPS LOCK':
        return 'key mod'
    if main_label.endswith(' LOCK'):
        main_label = main_label[:len(' LOCK')]
    if main_label in ('SHIFT', 'ALTGR', 'CTRL', 'ALT', 'SHIFTL', 'SHIFTR', 'CTRLR', 'CTRLL', 'CAPSSHIFT'):
        return 'key mod'
    return 'key'


class RenderContext:
    def __init__(self, x, y, *, scale, keymap=None):
        self.x = x
        self.y = y
        self.scale = scale
        self.m = 1
        self.keymap = keymap

    def shift(self, dx, dy):
        return RenderContext(self.x+dx, self.y+dy, scale=self.scale, keymap=self.keymap)

    def keysyms(self, keycode):
        return self.keymap.get(keycode, [])


def xml_escape(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def svg_label(text_x, label):
    if ' ' in label:
        words = label.split(' ')
        return f'<tspan x="{text_x}" dy="0">{xml_escape(words[0])}</tspan>' + ''.join(f'<tspan x="{text_x}" dy="1em">{xml_escape(word)}</tspan>' for word in words[1:])
    return xml_escape(label)


class Key:
    def __init__(self, keycode, *, width=1, height=1):
        global keys
        self._keycode = keycode
        self._width = width
        self._height = height

    def __repr__(self):
        args = [repr(self._keycode)]
        if self._width != 1:
            args.append(f'width={self._width}')
        if self._height != 1:
            args.append(f'height={self._height}')
        return f'Key({", ".join(args)})'

    def keys(self):
        return 1

    def render(self, ctx):
        keysyms = ctx.keysyms(self._keycode)
        labels = [keysym_label(keysym) for keysym in keysyms]
        label = main_label(labels)
        width = self._width*ctx.scale
        height = self._height*ctx.scale
        text_x = ctx.x + width/2
        text_y = ctx.y + height/2
        return (
            f'<g class="{key_classes(label)}" data-labels="{xml_escape(json.dumps(labels))}">' +
                f'<rect class="bg" x="{ctx.x + ctx.m}" y="{ctx.y + ctx.m}" width="{width - 2*ctx.m}" height="{height - 2*ctx.m}"/>' +
                f'<text class="lbl" x="{text_x}" y="{text_y}">{svg_label(text_x, label)}</text></g>',
            width, height,
        )


class ISOEnterKey:
    def __init__(self, keycode, width1, width2, height1, height2):
        self._keycode = keycode
        self._width1 = width1
        self._width2 = width2
        self._height1 = height1
        self._height2 = height2

    def __repr__(self):
        return f'ISOEnterKey({self._keycode}, {self._width1}, {self._width2}, {self._height1}, {self._height2})'

    def keys(self):
        return 1

    def _points(self, p_deltas, margin):
        p, deltas = p_deltas[0], p_deltas[1:]
        s = f'{p[0] + margin[0][0]},{p[1] + margin[0][1]}'
        for ((dx, dy), (mx, my)) in zip(deltas, margin[1:]):
            p = (p[0]+dx, p[1]+dy)
            s += f' {p[0] + mx},{p[1] + my}'
        return s

    def render(self, ctx):
        keysyms = ctx.keysyms(self._keycode)
        labels = [keysym_label(keysym) for keysym in keysyms]
        label = main_label(labels)
        width1 = self._width1*ctx.scale
        width2 = self._width2*ctx.scale
        height1 = self._height1*ctx.scale
        height2 = self._height2*ctx.scale
        p = self._points(
            [(ctx.x, ctx.y), (width1, 0), (0, height1+height2), (-width2, 0), (0, -height2), (-width1+width2, 0), (0, -height1)],
            [(ctx.m, ctx.m), (-ctx.m, ctx.m), (-ctx.m, -ctx.m), (ctx.m, -ctx.m), (ctx.m, -ctx.m), (ctx.m, -ctx.m), (ctx.m, ctx.m)],
        )
        return (
            f'<g class="{key_classes(label)}" data-labels="{xml_escape(json.dumps(labels))}">' +
                f'<polygon class="bg" points="{p}"/>' +
                f'<text class="lbl" x="{ctx.x + width1/2}" y="{ctx.y + height1/2}">{svg_label(ctx.x + width1/2, label)}</text></g>',
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

    def keys(self):
        return 0

    def render(self, ctx):
        return (f'', self._width*ctx.scale, self._height*ctx.scale)


class Row:
    def __init__(self, children):
        self._children = children

    def __repr__(self):
        return f'Row({", ".join(repr(child) for child in self._children)})'

    def keys(self):
        return sum(child.keys() for child in self._children)

    def render(self, ctx):
        svg, width, height = self._children[0].render(ctx)
        total_width = width
        for child in self._children[1:]:
            child_svg, child_width, child_height = child.render(ctx.shift(width, 0))
            if child_height != height:
                raise ValueError('Children have different heights: {} (height: {}) and {} (height: {})'.format(self._children[0], height, child, child_height))
            svg += child_svg
            total_width += child_width
            ctx = ctx.shift(child_width, 0)
        return svg, total_width, height


class TwoRowsISOEnter:
    def __init__(self, row1, row2, label, width1, width2):
        self._row1 = row1
        self._row2 = row2
        self._label = label
        self._width1 = width1
        self._width2 = width2

    def __repr__(self):
        return f'TwoRowsISOEnter({self._row1}, {self._row2}, {self._width1}, {self._width2})'

    def keys(self):
        return self._row1.keys() + self._row2.keys() + 1

    def render(self, ctx):
        row1_svg, row1_width, row1_height = self._row1.render(ctx)
        row2_svg, row2_width, row2_height = self._row2.render(ctx.shift(0, row1_height))
        total_row1_width = row1_width + self._width1*ctx.scale
        total_row2_width = row2_width + self._width2*ctx.scale
        if total_row1_width != total_row2_width:
            raise ValueError('Rows have different widths: {}+{} (width: {}) and {}+{} (width: {})'.format(row1_width, self._width1*ctx.scale, total_row1_width, row2_width, self._width2*ctx.scale, total_row2_width))
        enter_key = ISOEnterKey(self._label, self._width1, self._width2, row1_height/ctx.scale, row2_height/ctx.scale)
        enter_svg, enter_width, enter_height = enter_key.render(ctx.shift(row1_width, 0))
        return (
            row1_svg + row2_svg + enter_svg,
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

    def keys(self):
        return self._row1.keys() + self._row2.keys() + 1

    def render(self, ctx):
        row1_svg, row1_width, row1_height = self._row1.render(ctx)
        row2_svg, row2_width, row2_height = self._row2.render(ctx.shift(0, row1_height))
        if row1_width != row2_width:
            raise ValueError('Rows have different widths: {} (width: {}) and {} (width: {})'.format(self._row1, row1_width, self._row2, row2_width))
        key_svg, key_width, key_height = Key(self._label, height=(row1_height+row2_height)/ctx.scale).render(ctx.shift(row1_width, 0))
        return (
            row1_svg + row2_svg + key_svg,
            row1_width + key_width,
            row1_height + row2_height,
        )


class VBlock:
    def __init__(self, children):
        self._children = children

    def __repr__(self):
        return f'VBlock({", ".join(repr(child) for child in self._children)})'

    def keys(self):
        return sum(child.keys() for child in self._children)

    def render(self, ctx):
        svg, width, height = self._children[0].render(ctx)
        total_height = height
        for child in self._children[1:]:
            child_svg, child_width, child_height = child.render(ctx.shift(0, height))
            if child_width != width:
                raise ValueError('Children have different widths: {} (width: {}) and {} (width: {})'.format(self._children[0], width, child, child_width))
            svg += child_svg
            total_height += child_height
            ctx = ctx.shift(0, child_height)
        return svg, width, total_height


class HBlock:
    def __init__(self, *children):
        self._children = children

    def __repr__(self):
        return f'HBlock({", ".join(repr(child) for child in self._children)})'

    def keys(self):
        return sum(child.keys() for child in self._children)

    def render(self, ctx):
        svg, width, height = self._children[0].render(ctx)
        total_width = width
        for child in self._children[1:]:
            child_svg, child_width, child_height = child.render(ctx.shift(width, 0))
            if child_height != height:
                raise ValueError('Children have different heights: {} (height: {}) and {} (height: {})'.format(self._children[0], height, child, child_height))
            svg += child_svg
            total_width += child_width
            ctx = ctx.shift(child_width, 0)
        return svg, total_width, height


def default_keycode_keysyms(x, X, selected_columns):
    control = f'Control_{x.lower()}'
    keysyms = [
        f'+{x}', f'+{X}', f'+{x}', f'+{X}',
        control, control, control, control,
        f'Meta_{x}', f'Meta_{X}', f'Meta_{x}', f'Meta_{X}',
        f'Meta_{control}', f'Meta_{control}', f'Meta_{control}', f'Meta_{control}',
    ]
    keysyms *= 16
    result = ['VoidSymbol']*(selected_columns[-1] + 1)
    for column in selected_columns:
        if column >= len(result):
            raise ValueError(f'Column {column} is out of range -- only {len(result)} keysyms are defined')
        result[column] = keysyms[column]
    return result


def expand_one_keysym(keysym, selected_columns):
    c = keysym
    if c.startswith('+'):
        c = c[1:]
    if len(c) == 1 and 'A' <= c <= 'Z':
        return default_keycode_keysyms(c, c.lower(), selected_columns)
    if len(c) == 1 and 'a' <= c <= 'z':
        return default_keycode_keysyms(c, c.upper(), selected_columns)
    return [keysym]*(selected_columns[-1] + 1)


def load_keymap(filename, *, keymap=None):
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
                return modifier
        return ""

    columns = list(range(256))
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
            elif line.startswith('charset') or line.startswith('alt_is_meta') or line.startswith('string') or line.startswith('compose'):
                pass
            elif line.startswith('keycode'):
                line = line[len('keycode'):]
                code, definition = line.split('=')
                code = int(code.strip())
                definition = definition.split()
                if not definition:
                    keysyms = []
                elif len(definition) == 1:
                    keysym = definition[0]
                    keysyms = expand_one_keysym(keysym, columns)
                else:
                    keysyms = ['VoidSymbol']*(columns[-1] + 1)
                    for i, keysym in enumerate(definition):
                        column = columns[i]
                        keysyms[column] = keysym
                keymap[code] = keysyms
            elif starts_with_modifier(line) != "":
                column = 0
                while line and not line.startswith('keycode'):
                    modifier = starts_with_modifier(line)
                    column |= modifiers[modifier]
                    line = line[len(modifier):].lstrip()
                assert line.startswith('keycode')
                line = line[len('keycode'):].lstrip()
                code, keysym = line.split('=')
                code = int(code.strip())
                keysym = keysym.strip()
                if code not in keymap:
                    keymap[code] = []
                if column >= len(keymap[code]):
                    keymap[code].extend(['VoidSymbol']*(column - len(keymap[code]) + 1))
                keymap[code][column] = keysym
            elif line.startswith('keymaps'):
                columns_list = line[len('keymaps'):].strip().split(',')
                columns = []
                for column_range in columns_list:
                    if '-' in column_range:
                        start, end = column_range.split('-')
                        start = int(start)
                        end = int(end)
                        assert start <= end
                        assert not columns or start > columns[-1]
                        columns.extend(range(start, end+1))
                    else:
                        columns.append(int(column_range))
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
X1_ONE_ZERO_X3 = [Key(41)] + [Key(i) for i in range(2, 14)] + [Key(14, width=2)]  # `, 1, 2, ..., 0, -, =, Backspace
X1_Q_P_X2 = [Key(15, width=1.5)] + [Key(i) for i in range(16, 28)]  # Caps Lock, Q, W, ..., P, [, ]
X1_A_L_X2 = [Key(58, width=1.75)] + [Key(i) for i in range(30, 41)]  # A, S, ..., L, ;, '
Z_M_X4 = [Key(i) for i in range(44, 54)] + [Key(54, width=2.75)]  # Z, X, ..., M, comma, ., /, Right Shift

BOTTOM_ROW = [
    Key(29, width=1.25), Key(125, width=1.25), Key(56, width=1.25),
    Key(57, width=6.25),
    Key(100, width=1.25), Key(126, width=1.25), Key(127, width=1.25), Key(97, width=1.25),
]

SPECIAL_AND_DIRECTION_KEYS = [
    Row([Key(99), Key(70), Key(119)]),  # Print Screen, Scroll Lock, Pause
    Space(height=0.5, width=3),
    Row([Key(110), Key(102), Key(104)]),  # Insert, Home, Page Up
    Row([Key(111), Key(107), Key(109)]),  # Remove, End, Page Down
    Space(height=1, width=3),
    Row([Space(1), Key(103), Space(1)]),  # Up
    Row([Key(105), Key(108), Key(106)]),  # Left, Down, Right
]

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

KEYCODE_ENTER = 28
KEYCODE_LEFT_SHIFT = 42
KEYCODE_BACKSLASH = 43
KEYCODE_LESS = 86  # additional key on the 102/105 key layout

ANSI_LAYOUT = HBlock(
    VBlock([
        Row(ESC + [Space(1)] + F1_F4 + [Space(0.5)] + F5_F8 + [Space(0.5)] + F9_F12),
        Space(height=0.5, width=15),
        Row(X1_ONE_ZERO_X3),
        Row(X1_Q_P_X2 + [Key(KEYCODE_BACKSLASH, width=1.5)]),
        Row(X1_A_L_X2 + [Key(KEYCODE_ENTER, width=2.25)]),
        Row([Key(KEYCODE_LEFT_SHIFT, width=2.25)] + Z_M_X4),
        Row(BOTTOM_ROW),
    ]),
    Space(0.25, height=6.5),
    VBlock(SPECIAL_AND_DIRECTION_KEYS),
    Space(0.25, height=6.5),
    VBlock([Space(height=1.5, width=4)] + KEYPAD),
)

ISO_LAYOUT = HBlock(
    VBlock([
        Row(ESC + [Space(1)] + F1_F4 + [Space(0.5)] + F5_F8 + [Space(0.5)] + F9_F12), 
        Space(height=0.5, width=15),
        Row(X1_ONE_ZERO_X3),
        TwoRowsISOEnter(
            Row(X1_Q_P_X2),
            Row(X1_A_L_X2 + [Key(KEYCODE_BACKSLASH)]),
            KEYCODE_ENTER, 1.5, 1.25
        ),
        Row([Key(KEYCODE_LEFT_SHIFT, width=1.25), Key(KEYCODE_LESS)] + Z_M_X4),
        Row(BOTTOM_ROW),
    ]),
    Space(0.25, height=6.5),
    VBlock(SPECIAL_AND_DIRECTION_KEYS),
    Space(0.25, height=6.5),
    VBlock([Space(height=1.5, width=4)] + KEYPAD),
)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Render a keyboard layout to SVG.')
    parser.add_argument('--iso', action='store_true', help='Render an ISO layout.')
    parser.add_argument('--scale', type=int, default=60, help='The scale of the rendered layout.')
    parser.add_argument('keymap', help='The keymap file to use.')
    args = parser.parse_args()

    layout = ISO_LAYOUT if args.iso else ANSI_LAYOUT
    svg, width, height = layout.render(RenderContext(0, 0, scale=args.scale, keymap=load_keymap(args.keymap)))
    script = """let currentColumn = 0;
let capsLock = false;
function mod(label) {
  if (label.endsWith(" LOCK")) {
    label = label.substring(0, label.length - " LOCK".length);
  }
  switch (label) {
    case "SHIFT": return 1;
    case "ALTGR": return 2;
    case "CTRL": return 4;
    case "ALT": return 8;
    case "SHIFTL": return 16;
    case "SHIFTR": return 32;
    case "CTRLR": return 64;
    case "CTRLL": return 128;
    case "CAPSSHIFT": return 256;
    default: return 0;
  }
}
function escapeXML(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
function switchColumn(column) {
  currentColumn = column;
  const keys = document.querySelectorAll(".key");
  for (const key of keys) {
    const labels = JSON.parse(key.getAttribute("data-labels"));
    let label = currentColumn < labels.length ? labels[currentColumn] : "";
    if (label.length > 1 && label[0] == "+") {
      if (capsLock) {
        let shiftColumn = currentColumn ^ 1;
        label = shiftColumn < labels.length ? labels[shiftColumn] : "";
        if (label.length > 1 && label[0] == "+") {
          label = label.substring(1);
        }
      } else {
        label = label.substring(1);
      }
    }
    if (label == "CAPS LOCK") {
      if (capsLock) {
        key.classList.add("active");
      } else {
        key.classList.remove("active");
      }
    } else {
      let modColumn = mod(label);
      if (modColumn) {
        if (currentColumn & modColumn) {
          key.classList.add("active");
        } else {
          key.classList.remove("active");
        }
      }
    }
    const lbl = key.querySelector(".lbl");
    if (label.indexOf(" ") != -1) {
      tspans = "";
      label.split(" ").forEach((word, i) => {
        if (i == 0) {
          tspans += `<tspan x="${lbl.getAttribute("x")}" dy="0">${escapeXML(word)}</tspan>`;
        } else {
          tspans += `<tspan x="${lbl.getAttribute("x")}" dy="1em">${escapeXML(word)}</tspan>`;
        }
      });
      lbl.innerHTML = tspans;
    } else {
      lbl.innerHTML = escapeXML(label);
    }
  }
}
window.addEventListener("DOMContentLoaded", () => {
  const keys = document.querySelectorAll(".key");
  for (const key of keys) {
    key.addEventListener("click", (e) => {
      const labels = JSON.parse(key.getAttribute("data-labels"));
      const label = currentColumn < labels.length ? labels[currentColumn] : "";
      if (label == "CAPS LOCK") {
        capsLock = !capsLock;
        switchColumn(currentColumn);
      } else {
        const modColumn = mod(label);
        if (modColumn) {
          switchColumn(currentColumn ^ modColumn);
        }
      }
    });
  }
});"""
    print(f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="{width+3}" height="{height+3}" viewBox="-1 -1 {width+2} {height+2}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<style>
.mod{{cursor:pointer}}
.mod .bg{{fill:#ddd}}
.active .bg{{fill:#fd9}}
.bg{{fill:#eee;stroke:#ccc;stroke-linejoin:round}}
.lbl{{fill:#333;text-anchor:middle;text-align:center}}
</style>
<script><![CDATA[
{script}
]]></script>
<g font-family="Arial" font-size="{args.scale // 4}px" font-size-adjust="0.518"><g>''' + svg + '''</g></g>
</svg>''')


if __name__ == '__main__':
    main()
