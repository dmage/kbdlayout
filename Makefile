KEYMAPS = cz.map defkeymap.map fr.map ruwin_alt-UTF-8.map uk.map

examples:
	mkdir -p ./examples
	echo '<ul>' >./examples/index.html
	for keymap in $(KEYMAPS); do \
		./kbd-layout.py ./keymaps/$$keymap >./examples/$$keymap-ansi.svg; \
		./kbd-layout.py --iso ./keymaps/$$keymap >./examples/$$keymap-iso.svg; \
		echo "<li><a href=\"$$keymap-ansi.svg\">$$keymap (ANSI)</a></li>" >>./examples/index.html; \
		echo "<li><a href=\"$$keymap-iso.svg\">$$keymap (ISO)</a></li>" >>./examples/index.html; \
	done
	echo '</ul>' >>./examples/index.html
.PHONY: examples
