from libqtile import widget
from qtile_extras import widget as extra_widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration

from themes import Theme

theme = Theme.get_theme(Theme.get_current_qtile_theme())

# Theme colors
BACKGROUND = theme.background
FOREGROUND = theme.foreground
PRIMARY = theme.primary
SECONDARY = theme.secondary
HIGHLIGHT = theme.highlight
ACCENT = theme.warning  # Using warning color as accent
GLOW = theme.glow
PULSE = theme.pulse

# ===== Modern Decorations =====
modern_decoration = {
    "decorations": [
        RectDecoration(
            colour=GLOW, radius=8, filled=True, padding_x=6, padding_y=2, extrawidth=4
        )
    ]
}

minimal_decoration = {
    "decorations": [
        RectDecoration(
            colour=f"{GLOW}40", radius=6, filled=True, padding_x=4, padding_y=0
        )
    ]
}

divider_decoration = {
    "decorations": [
        PowerLineDecoration(path="forward_slash", color=f"{FOREGROUND}20", size=12)
    ]
}


# ===== Modern Widgets =====
def left_widgets():
    """Widgets for left-aligned bar"""
    return [
        # ---- Logo ----
        widget.TextBox(
            text="",  # Arch Linux logo
            foreground=PRIMARY,
            fontsize=20,
            padding=12,
            **modern_decoration,
        ),
        # ---- Group Box ----
        widget.GroupBox(
            foreground=FOREGROUND,
            active=PRIMARY,
            inactive="#3a3a5a",
            block_highlight_text_color=FOREGROUND,
            highlight_method="block",
            this_current_screen_border=HIGHLIGHT,
            borderwidth=0,
            padding_x=8,
            spacing=8,
            urgent_alert_method="block",
            urgent_text=ACCENT,
            **divider_decoration,
        ),
        widget.Spacer(length=8),
        # ---- Prompt -----
        widget.Prompt(prompt=">",
                      cursor_color=FOREGROUND)
    ]


def right_widgets():
    """Widgets for right-aligned bar"""
    return [
        # ---- System Tray ----
        widget.Systray(icon_size=18, padding=8, background=f"{GLOW}30"),
        # ---- CPU ----
        widget.CPU(
            foreground=PRIMARY,
            format=" {load_percent}%",
            padding=8,
            **minimal_decoration,
        ),
        # ---- Temperature ----
        widget.ThermalSensor(
            foreground=FOREGROUND,  # Normal text color
            foreground_alert=" #e73a15",  # Color when threshold is exceeded
            tag="coretemp",  # Try 'k10temp' for AMD or 'cpu_thermal' for Pi
            threshold=80,
            fmt="🌡️ {}",
            padding=5,
            update_interval=5,
        ),
        # ---- Memory ----
        widget.Memory(
            foreground=SECONDARY,
            format=" {MemUsed:.1f}G",
            measure_mem="G",
            padding=8,
            **minimal_decoration,
        ),
        # ---- Clock ----
        widget.Clock(
            foreground=HIGHLIGHT, format=" %H:%M", padding=10, **minimal_decoration
        ),
        # ---- Date ----
        widget.Clock(
            foreground=FOREGROUND, format=" %a %d", padding=10, **minimal_decoration
        ),
        # ---- Layout Icon ----
        widget.CurrentLayoutIcon(
            scale=0.7, foreground=SECONDARY, padding=8, **minimal_decoration
        ),
    ]
