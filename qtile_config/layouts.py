from libqtile import layout

layouts = [
    layout.Max(),
    layout.Tile(ratio=0.50, add_on_top=False),
]

floating_layout = layout.Floating(
    auto_float_types=[
        "notification",
        "toolbar",
        "splash",
        "dialog",],
    float_rules = [dict(wmclass="spotify")])
