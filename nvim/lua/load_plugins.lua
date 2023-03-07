-- Basically specifying the plugins that want to be used

return require('packer').startup(function(use)

    use 'wbthomason/packer.nvim'

    use {
        'nvim-tree/nvim-tree.lua',
        requires = 'nvim-tree/nvim-web-devicons'
    }

    use 'nvim-lualine/lualine.nvim'

    use 'lukas-reineke/indent-blankline.nvim'

    use 'windwp/nvim-autopairs'

    use 'akinsho/toggleterm.nvim'

    use 'ellisonleao/gruvbox.nvim'

end)
