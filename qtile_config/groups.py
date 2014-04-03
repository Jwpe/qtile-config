from libqtile.command import lazy
from libqtile.config import Group, Key

from .modifiers import mod

groups = [
    Group("a"),
    Group("d"),
    Group("f"),
    Group("u"),
    Group("i"),
    Group("o"),
]

group_keys = []

for i in groups:
    # mod1 + letter of group = switch to group
    group_keys.append(
        Key([mod], i.name, lazy.group[i.name].toscreen())
    )

    # mod1 + shift + letter of group = switch to & move focused window to group
    group_keys.append(
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name))
    )
