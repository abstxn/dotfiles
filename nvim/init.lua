-- vim.g.mapleader = " "
-- vim.api.nvim_set_keymap('i', 'jk', '<ESC>', { noremap = true })

-- Searches '~/.config/nvim/lua/' for modules.
require 'keybinds'
require 'options'
require 'plugins'

-- ~/.config/nvim/plugin/ --> contains plugin specific Lua code
