from libqtile.config import Screen
from libqtile import bar, widget

widget_defaults = {
    'font': 'Ubuntu Mono'
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(**widget_defaults),
                widget.Prompt(**widget_defaults),
                widget.WindowName(**widget_defaults),
                widget.Volume(**widget_defaults),
                widget.Battery(
                         energy_now_file='charge_now',
                         energy_full_file='charge_full',
                         power_now_file='current_now',
                         **widget_defaults
                     ),
                widget.Systray(),
                widget.Clock('%Y-%m-%d %a %I:%M %p', **widget_defaults),
            ],
            20,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(**widget_defaults),
                widget.Prompt(**widget_defaults),
                widget.WindowName(**widget_defaults),
            ],
            20,
        ),
    ),
]
