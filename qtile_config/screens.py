from libqtile.config import Screen
from libqtile import bar, widget

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Volume(),
                widget.Battery(
                    energy_now_file='charge_now',
                    energy_full_file='charge_full',
                    power_now_file='current_now',

                ),
                widget.Systray(),
                widget.TextBox("Local Time:"),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p', ),
                widget.TextBox("US Time:"),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p', timezone="US/Eastern"),
            ],
            25,
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.TextBox("CPU:"),
                widget.CPUGraph(samples=400, width=400),
                widget.TextBox("RAM:"),
                widget.MemoryGraph(samples=400, width=400),
            ],
            25,
        ),
    ),
]
