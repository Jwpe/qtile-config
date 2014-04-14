from libqtile.config import Key
from libqtile.command import lazy

from .modifiers import mod

command_keys = [
    # Switch screens
    Key(
        [mod], "1",
        lazy.to_screen(0),
        lazy.group.toscreen(0)
    ),
    Key(
        [mod], "2",
        lazy.to_screen(1),
        lazy.group.toscreen(1)
    ),

    # Switch between windows in current stack pane
    Key(
        [mod], "k",
        lazy.layout.down()
    ),
    Key(
        [mod], "j",
        lazy.layout.up()
    ),

    # Move windows up or down in current stack
    Key(
        [mod, "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.shuffle_up()
    ),

    # Widen or shrink a pane
    Key([mod], "bracketright", lazy.layout.increase_ratio()),
    Key([mod], "bracketleft", lazy.layout.decrease_ratio()),

    # Switch window focus to other pane(s) of stack
    Key(
        [mod], "Tab",
        lazy.layout.next()
    ),

    # Swap panes of split stack
    Key(
        [mod, "shift"], "space",
        lazy.layout.rotate()
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split()
    ),

    # Toggle between different layouts as defined below
    Key([mod], "space",    lazy.nextlayout()),
    Key([mod], "w",      lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod], "Delete", lazy.shutdown()),

    # Spawn programs
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "Return", lazy.spawn("gnome-terminal")),
    Key([mod], "c", lazy.spawn("google-chrome")),
    Key([mod], "s", lazy.spawn("subl")),
    Key([mod], "x", lazy.spawn("xchat")),
    Key([mod], "h", lazy.spawn("hipchat")),
    Key([mod], "m", lazy.spawn("spotify")),

    # Volume control
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Screenshot
    Key([mod], "Insert", lazy.spawn("sleep 0.2; scrot -e 'mv $f /home/jonathan/Pictures/screenshots' -s")),
]
