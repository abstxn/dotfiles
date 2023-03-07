-- disable netrw at the very start of your init.lua (strongly advised)
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1


-- Load Lua scripts

require 'load_plugins'	-- "Hey, we're going to need these plugins!"

require 'settings/vim'
require 'settings/nvim_tree'
require 'settings/nvim_autopairs'
require 'settings/lualine'
require 'settings/toggleterm'
require 'settings/colorscheme'
