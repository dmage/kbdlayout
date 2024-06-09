KEYMAPS = cz.map defkeymap.map ruwin_alt-UTF-8.map uk.map

examples:
	mkdir -p ./examples
	for keymap in $(KEYMAPS); do \
		./kbd-layout.py ./keymaps/$$keymap > ./examples/$$keymap.svg; \
	done
.PHONY: examples
