# Allow me to store my stuff in a package
from os import sys, path
from libqtile import hook
import subprocess

sys.path.append(
    path.abspath(path.join(path.dirname(__file__), 'qtile_config'))
)

from qtile_config.groups import groups, group_keys
from qtile_config.keys import command_keys
from qtile_config.layouts import layouts, floating_layout
from qtile_config.screens import screens


@hook.subscribe.startup_once
def autostart():
    home = path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

keys = group_keys + command_keys

dgroups_key_binder = None
dgroups_app_rules = []

main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
mouse = ()
auto_fullscreen = True

widget_defaults = {
    'font': 'Ubuntu Mono'
}
