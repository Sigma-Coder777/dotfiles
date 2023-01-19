from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os, subprocess

mod = "mod4"

terminal ="alacritty -e fish" # fish & alacritty <3
browser = "firefox" # Firefox with cascade custom userChrome.css <3
second_browser = "brave" # Yet another great browser
file_manager = "pcmanfm"
screenshot_tool = "flameshot gui"

#This script will execute every single time either you reload qtile config or login
#Don"t add your apps like discord here. Thank me later :)
start_always ='~/.config/qtile/autostart.sh'
#Add the path of the script you want to run only when you login
#Un-Comment the hook at the last of this file
start_once = "~/.config/qtile/start_once.sh"
group_names = '   ﭮ   祥 '.split()

keys = [

    # Switch between windows
    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"),
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "control"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "control"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "control"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "control"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"),

    Key([mod,"shift"],"h",
        lazy.layout.shrink(),
        desc="Shrinks the window in monadtall"),
    Key([mod,"shift"],"l",
        lazy.layout.grow(),
        desc="grows the window in monadtall"),
    Key([mod],"f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle Fullscreen"),



   #Application launching Keybinds
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"),
    Key([mod], "b",
        lazy.spawn(browser),
        desc=f"Launch {browser}"),
    Key([mod], "e",
        lazy.spawn(file_manager),
        desc=f"Launch {file_manager}"),
    Key([mod, "shift"], "b",
        lazy.spawn(second_browser),
        desc=f"Launch {second_browser}"),
    Key([mod,"shift"], "d",
        lazy.spawn("rofi -show drun"),
        desc="Launch Rofi"),
    Key([mod], "p",
        lazy.spawn("pavucontrol"),
        desc="Launch Pavucontrol"),
    Key([mod], "s",
        lazy.spawn(screenshot_tool),
        desc="Launches the screenshot utility"),

    # Toggle between different layouts as defined below
    Key([mod], "space",
        lazy.next_layout(),
        desc="Toggle between layouts"),
    Key([mod, "shift"], "c",
        lazy.window.kill(),
        desc="Kill focused window"),
    Key([mod, "control"], "r",
        lazy.reload_config(),
        desc="Reload the config"),
    Key([mod, "control"], "q",
        lazy.shutdown(), desc="Shutdown Qtile"),
]

#This Function is responsible for changing names of the groups
#By Default it assigns monadtall layout to all of the groups/workspaces
groups = [Group(name, layout='monadtall') for name in group_names]
for i, name in enumerate(group_names):
    indx = str(i + 1)
    keys += [
        Key([mod], indx, lazy.group[name].toscreen()),
        Key([mod, 'shift'], indx, lazy.window.togroup(name))
    ]

layouts = [
    layout.MonadTall(border_focus="#ADD8E6",border_width=2,margin=7),
    layout.Max(),
    layout.Floating(border_focus="#ADD8E6"),
    layout.Tile(border_focus="#ADD8E6",border_width=2,margin=7),
    ]
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

screens = [
    Screen()
]

mouse = [
    Drag([mod], "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod,"shift"],
         "Button1",
         lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button1",
          lazy.window.bring_to_front()),
]

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
wmname = "LG3D"

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser(start_always)
    subprocess.Popen([home])

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser(start_once)
    subprocess.Popen([home])
