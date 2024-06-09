KEYMAPS = cz.map defkeymap.map fr.map ruwin_alt-UTF-8.map uk.map

examples:
	mkdir -p ./examples
	for keymap in $(KEYMAPS); do \
		./kbd-layout.py ./keymaps/$$keymap > ./examples/$$keymap-ansi.svg; \
		./kbd-layout.py --iso ./keymaps/$$keymap > ./examples/$$keymap-iso.svg; \
	done
.PHONY: examples
