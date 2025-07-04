#!/usr/bin/env python3
import os
import re

import toml

from themes import Theme

# Path to your Alacritty config file
ALACRITTY_CONFIG = os.path.expanduser("~/.config/alacritty/alacritty.toml")
QTILE_CONFIG = os.path.expanduser("~/.config/qtile/config.py")


def main():
    # Get current Qtile theme (default to 'gruvbox' as in your config)
    current_theme = Theme.get_current_qtile_theme()
    # Update Alacritty config
    update_alacritty_theme(current_theme)


def update_alacritty_theme(theme_name: str):
    """Update Alacritty config with colors from the specified theme"""
    theme = Theme.get_theme(theme_name)

    # Alacritty color mapping for TOML format
    alacritty_colors = {
        "colors": {
            "primary": {
                "background": theme.background,
                "foreground": theme.foreground,
            },
            "cursor": {
                "text": theme.background,
                "cursor": theme.primary,
            },
            "normal": {
                "black": "#1e222a",  # Dark background variant
                "red": theme.warning,
                "green": theme.highlight,
                "yellow": theme.pulse,
                "blue": theme.primary,
                "magenta": theme.secondary,
                "cyan": "#56b6c2",  # Complementary color
                "white": theme.foreground,
            },
            "bright": {
                "black": "#3e4452",  # Lighter background variant
                "red": "#ff6b6b",  # Brighter warning
                "green": "#98c379",  # Brighter highlight
                "yellow": "#e5c07b",  # Brighter pulse
                "blue": "#61afef",  # Brighter primary
                "magenta": "#c678dd",  # Brighter secondary

                "cyan": "#56b6c2",  # Brighter complementary
                "white": "#abb2bf",  # Brighter foreground
            },
            "indexed_colors": [
                {"index": 16, "color": theme.pulse},  # Example mapping
                {"index": 17, "color": theme.warning},
                {"index": 18, "color": "#303030"},
                {"index": 19, "color": "#353535"},
                {"index": 20, "color": "#b2ccd6"},
                {"index": 21, "color": "#eeffff"},
            ],
        }
    }

    # Read existing Alacritty config
    try:
        with open(ALACRITTY_CONFIG, "r") as f:
            config = toml.load(f)
    except FileNotFoundError:
        config = {}

    # Preserve non-color sections
    preserved_sections = {
        "env": config.get("env", {}),
        "font": config.get("font", {}),
        "keyboard": config.get("keyboard", {}),
        "window": config.get("window", {}),
        "general": config.get("general", {}),
    }

    # Merge colors with preserved config
    updated_config = {**preserved_sections, **alacritty_colors}

    # Write back to config file
    with open(ALACRITTY_CONFIG, "w") as f:
        toml.dump(updated_config, f)

    print(f"Updated Alacritty config with {theme.name} theme")


if __name__ == "__main__":
    main()
