return require('packer').startup(function(use)
	use 'wbthomason/packer.nvim'
	use 'gruvbox-community/gruvbox'
    use {
        'catppuccin/nvim',
        as = 'catppuccin'
    }
    use 'nvim-lualine/lualine.nvim'
    use {
        'nvim-tree/nvim-tree.lua',
        requires = {
            'nvim-tree/nvim-web-devicons' -- optional, for file icons
        }
    }
    use 'lukas-reineke/indent-blankline.nvim'
    use {
        'phaazon/hop.nvim',
        branch = 'v2', -- optional but strongly recommended
        config = function()
            -- you can configure Hop the way you like here; see :h hop-config
            require'hop'.setup { keys = 'etovxqpdygfblzhckisuran' }
        end
    }
    use {
        "akinsho/toggleterm.nvim",
        tag = 'v2.2.1'
    }
    use "windwp/nvim-autopairs"
end)
