from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

# Global Variables
terminal = "kitty"

#  _  __                 _       _               _       
# | |/ /   ___   _   _  | |__   (_)  _ __     __| |  ___ 
# | ' /   / _ \ | | | | | '_ \  | | | '_ \   / _` | / __|
# | . \  |  __/ | |_| | | |_) | | | | | | | | (_| | \__ \
# |_|\_\  \___|  \__, | |_.__/  |_| |_| |_|  \__,_| |___/
#                |___/                                   
# keybinds, shortcuts, hotkeys

mod = "mod4"

keys = [
    # Focus
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    # Move Windows
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Resize Windows
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),

    # System
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.spawn("rofi -show power-menu -modi power-menu:'rofi-power-menu --no-symbols'")),
    # Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Rofi
    Key([mod], "space", lazy.spawn("rofi -show combi"), desc="Launch Rofi"),
    Key([mod, "control"], "e", lazy.spawn("rofi -show emoji -emoji-mode menu"), desc="Emoji selector"),

    # Audio
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Screenshots
    Key([], "Print", lazy.spawn("/home/abstxn/scripts/shoot_and_copy.sh")),

    # Layouts
    Key([mod], "p", lazy.next_layout()),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    # Stack Layout Specific Commands
    Key([mod], "o", lazy.layout.toggle_split()),
    Key([mod], "h", lazy.layout.previous()),
    Key([mod], "l", lazy.layout.next()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "l", lazy.layout.client_to_next()),
    Key([mod, "shift"], "h", lazy.layout.client_to_previous()),
    Key([mod], "equal", lazy.layout.add()),
    Key([mod], "minus", lazy.layout.delete()),
]

#   ____                                      
#  / ___|  _ __    ___    _   _   _ __    ___ 
# | |  _  | '__|  / _ \  | | | | | '_ \  / __|
# | |_| | | |    | (_) | | |_| | | |_) | \__ \
#  \____| |_|     \___/   \__,_| | .__/  |___/
#                                |_|          
# workspaces

groups = [Group(i) for i in "123456789"]

for group in groups:
    keys.extend([
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
    ])

#   ____           _                      
#  / ___|   ___   | |   ___    _ __   ___ 
# | |      / _ \  | |  / _ \  | '__| / __|
# | |___  | (_) | | | | (_) | | |    \__ \
#  \____|  \___/  |_|  \___/  |_|    |___/
#                                         
# colors, colours

# Use custom colors
bg = '#282828'
bg_alt = '#665c54'
accent = '#d65d0e'
fg = '#ebdbb2'

#  ____                          _            _                           _       
# / ___|    ___   _ __    __ _  | |_    ___  | |__    _ __     __ _    __| |  ___ 
# \___ \   / __| | '__|  / _` | | __|  / __| | '_ \  | '_ \   / _` |  / _` | / __|
#  ___) | | (__  | |    | (_| | | |_  | (__  | | | | | |_) | | (_| | | (_| | \__ \
# |____/   \___| |_|     \__,_|  \__|  \___| |_| |_| | .__/   \__,_|  \__,_| |___/
#                                                    |_|                          
# scratchpads

# Define scratchpads.
groups.append(ScratchPad('scratchpad',[
        DropDown(
            'term', 'kitty',
            width=0.4, height=0.5,
            x=0.3, y=0.1,
            opacity=1
        ),
        DropDown(
            'mixer', 'pavucontrol',
            width=0.3, height=0.4,
            x=0.35, y=0.1,
            opacity=1
        ),
        DropDown(
            'blueman', 'blueman-manager',
            width=0.3, height=0.4,
            x=0.35, y=0.1,
            opacity=1
        ),
        DropDown(
            'files', 'nemo',
            width=0.4, height=0.5,
            x=0.3, y=0.1,
            opacity=1
        ),
]))

# Keybinds to open scratchpads.
keys.extend([
    Key([mod], "return", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('mixer')),
    Key([mod], "b", lazy.group['scratchpad'].dropdown_toggle('blueman')),
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('files')),
])

#  _                                       _         
# | |       __ _   _   _    ___    _   _  | |_   ___ 
# | |      / _` | | | | |  / _ \  | | | | | __| / __|
# | |___  | (_| | | |_| | | (_) | | |_| | | |_  \__ \
# |_____|  \__,_|  \__, |  \___/   \__,_|  \__| |___/
#                  |___/                             

bw = 2

monadtall_layout = layout.MonadTall(
    # border_focus=accent,
    border_normal=bg,
    margin=12,
    border_width=bw,
    single_margin=36,
    single_border_width=0,
)

stack_layout = layout.Stack(
    autosplit=True,
    border_focus='#00ff00',
    border_normal=bg,
    margin=8,
    border_width=bw,
    num_stacks=2,
    fair=True,
)

max_layout = layout.Max(
    margin=32,
    border_width=bw,
    border_focus=accent,
)

monocle_layout = layout.Max(
    # margin=64,
    margin=[64, 256, 64, 256],
    border_width=0,
    # border_focus=accent,
)

layouts = [
    max_layout,
    # monocle_layout,
    stack_layout,
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="pavucontrol"),  # GPG key password entry
    ],
    border_focus=accent,
    border_normal=bg,
    border_width=bw,
)

#  ____    _             _                     ____                 
# / ___|  | |_    __ _  | |_   _   _   ___    | __ )    __ _   _ __ 
# \___ \  | __|  / _` | | __| | | | | / __|   |  _ \   / _` | | '__|
#  ___) | | |_  | (_| | | |_  | |_| | \__ \   | |_) | | (_| | | |   
# |____/   \__|  \__,_|  \__|  \__,_| |___/   |____/   \__,_| |_|   
#                                                                   
# status bar, widgets

widget_defaults = dict(
    font="JetBrainsMonoNL NFM",
    fontsize=14,
    padding=2,
    foreground=fg,
)
extension_defaults = widget_defaults.copy()

separator = widget.Sep(padding=20, linewidth=1, foreground=bg_alt, size_percent=70)
group_nav = widget.GroupBox(
        highlight_method="border", borderwidth=2, rounded=False,
        urgent_alert_method="text",
        this_current_screen_border=bg_alt,  # current focused group
        inactive=bg_alt,                    # no windows
        active=fg,                          # contains window(s)
        padding_x=3, padding_y=1,
        disable_drag=True,
)
current_apps =  widget.TaskList(
        highlight_method="border", borderwidth=2, rounded=False, border=bg_alt,
        margin_x=1, margin_y=1, padding_x=6, padding_y=1,
        max_title_width=2**8, icon_size=16,
)

screens = [
    Screen(
        top=bar.Bar(
            widgets=[
                group_nav,
                separator,
                # widget.CurrentLayoutIcon(scale=0.65),
                widget.CurrentLayout(),
                separator,
                current_apps,
                widget.Systray(),
                separator,
                widget.Volume(step=1, fmt="󰕾 {}"),
                separator,
                widget.Clock(format="%H:%M %p"),
                separator,
                widget.Clock(format="%A, %d %b %Y", ),
                widget.Spacer(length=8),
            ],
            size=24,
            margin=[0,0,0,0],
            background=bg,
        ),
    ),
]


#  __  __   _                  
# |  \/  | (_)  ___    ___     
# | |\/| | | | / __|  / __|    
# | |  | | | | \__ \ | (__   _ 
# |_|  |_| |_| |___/  \___| (_)
#                              

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = 'floating_only'
cursor_warp = False
auto_fullscreen = True
auto_minimize = True
focus_on_window_activation = "smart"
reconfigure_screens = True
# Required for edge case of Java UI toolkits.
# "LG3D" happens to be on Java's whitelist.
wmname = "Qtile"
