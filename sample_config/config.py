import os
import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from key_bindings import keys
from screen_widgets import left_widgets, right_widgets
from themes import Theme

# ===== Colour Theme =====
theme = Theme.get_theme("interstellar")  # Change to "dracula", "nord", etc.

# Theme colors
BACKGROUND = theme.background
FOREGROUND = theme.foreground
PRIMARY = theme.primary
SECONDARY = theme.secondary
HIGHLIGHT = theme.highlight
WARNING = theme.warning

MOD = "MOD4"

# ===== Core Settings =====
dgroups_key_binder = None
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"


# ===== Groups =====
def init_groups():
    """Groups with modern minimalist labels"""
    return [
        Group(name="1", label=""),  # Terminal icon
        Group(name="2", label=""),  # Browser icon
        Group(name="3", label=""),  # Code icon
        Group(name="4", label=""),  # Chat icon
        Group(name="5", label=""),  # Music icon
        Group(name="6", label=""),  # Folder icon
        Group(name="0", label=""),  # Settings icon
        Group(name="9", label=""),  # Hardware monitor icon
    ]


# Keybindings for group switching


for i in init_groups():
    keys.extend(
        [
            # ... existing code above ...
            Key(
                [MOD],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            Key(
                [MOD, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc=f"Move window to group {i.name}",
            ),
        ]
    )


# ===== Layouts =====
def init_layouts():
    """Modern layouts with subtle glow effects"""
    return [
        layout.MonadTall(
            border_focus=PRIMARY,
            border_normal="#1a1a2a",
            border_width=2,
            margin=8,
            single_border_width=0,
        ),
        layout.Max(),
        layout.Floating(
            border_focus="#00000000",
            border_normal="#00000000",
            border_width=2,
        ),
        layout.Matrix(
            border_focus="#00000000", border_normal="#00000000", columns=2, margin=8
        ),
    ]


# ===== Screens & Bar =====
def init_screens():
    """Modern top bar with split widget alignment"""
    return [
        Screen(
            top=bar.Bar(
                left_widgets() + [widget.Spacer()] + right_widgets(),
                size=30,
                margin=[8, 12, 4, 12],  # Unified margins
                background="#00000000",
                border_color="#00000000",
                border_width=[0, 0, 0, 0],
                opacity=1,
            )
        )
    ]


# ===== Mouse =====
def init_mouse():
    return [
        Drag(
            [MOD],
            "Button1",
            lazy.window.set_position_floating(),
            start=lazy.window.get_position(),
        ),
        Drag(
            [MOD],
            "Button3",
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        Click([MOD], "Button2", lazy.window.bring_to_front()),
    ]


# ===== Floating Windows =====
def floating():
    return layout.Floating(
        float_rules=[
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset|makebranch|maketag|ssh-askpass"),
            Match(title="branchdialog|pinentry"),
            Match(wm_class="sysmon"),
        ],
        border_focus="#00000000",
        border_normal="#00000000",
    )


# ===== Autostart =====
@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([os.path.expanduser("~/.config/qtile/scripts/auto_start.sh")])


@hook.subscribe.startup
def spawn_hardware_monitors():
    # Spawn hardware monitors in group 9
    monitors = [
        "alacritty --class=sysmon,htop -e htop",
        "alacritty --class=sysmon,btm -e btm",
        "alacritty --class=sysmon,nvtop -e nvtop",
    ]
    for cmd in monitors:
        try:
            subprocess.Popen(cmd.split())
        except:
            pass


@hook.subscribe.client_new
def assign_hardware_group(window):
    if "sysmon" in window.get_wm_class():
        window.togroup("9")
        window.cmd_disable_floating()


@hook.subscribe.startup
def sync_alacritty_theme():
    subprocess.Popen([os.path.expanduser("~/.config/qtile/sync_alacritty.py")])




# ===== Final Export =====
if __name__ in ["config", "__main__"]:
    keys = keys
    groups = init_groups()
    layouts = init_layouts()
    screens = init_screens()
    mouse = init_mouse()
    floating_layout = floating()
