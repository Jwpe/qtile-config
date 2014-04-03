from libqtile import layout

layouts = [
    layout.Max(),
    layout.xmonad.MonadTall(ratio=0.50),
    layout.Tile(ratio=0.50, masterWindows=2),
]

floating_layout = layout.Floating(auto_float_types=[
  "notification",
  "toolbar",
  "splash",
  "dialog",
])
