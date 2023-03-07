vim.o.number = true
vim.o.linebreak = true

vim.o.expandtab = true -- insert spaces when using tab
vim.o.tabstop = 4 -- number of spaces in a tab
vim.o.shiftround = true -- round the tab to a multiple of `shiftwidth`
vim.o.shiftwidth = 4 -- ^

vim.o.swapfile = false

vim.api.nvim_set_keymap('i', 'jk', '<ESC>', { noremap = true })
