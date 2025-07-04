# themes.py
import os
import re
from typing import Dict, List, Tuple

# Path to your qtile config
QTILE_CONFIG = os.path.expanduser("~/.config/qtile/config.py")


class Theme:
    def __init__(
        self,
        name: str,
        background: str,
        foreground: str,
        primary: str,
        secondary: str,
        highlight: str,
        warning: str,
        glow: str,
        pulse: str,
    ):
        self.name = name
        self.background = background
        self.foreground = foreground
        self.primary = primary
        self.secondary = secondary
        self.highlight = highlight
        self.warning = warning
        self.glow = glow
        self.pulse = pulse

    @staticmethod
    def get_theme(theme_name: str = "gruvbox"):
        """Get a theme by name (defaults to gruvbox if not found)"""
        return THEMES.get(theme_name.lower(), THEMES["gruvbox"])

    @staticmethod
    def get_current_qtile_theme():
        """Extract the current theme name from Qtile's config.py"""
        try:
            with open(QTILE_CONFIG, "r") as f:
                config_content = f.read()

            # Search for theme = get_theme("theme_name") pattern
            match = re.search(
                r'theme\s*=\s*get_theme\(["\']([^"\']+)["\']\)', config_content
            )
            if match:
                return match.group(1)

            # Alternative pattern if the above fails
            match = re.search(r'get_theme\(["\']([^"\']+)["\']\)', config_content)
            if match:
                return match.group(1)

        except FileNotFoundError:
            print(f"Error: Qtile config not found at {QTILE_CONFIG}")

        return "gruvbox"  # Fallback theme


# ===== Modern Dark Themes =====
THEMES = {
    # Cyberpunk Neon Theme - Enhanced with brighter neons
    "cyberpunk": Theme(
        name="Cyberpunk Neon",
        background="#000010",  # Near-black with blue tint
        foreground="#f0f8ff",  # Bright ice blue
        primary="#00f2fe",  # Electric cyan
        secondary="#ff00ff",  # Pure magenta
        highlight="#00ff9d",  # Vivid mint green
        warning="#ff2a6d",  # Hot pink
        glow="#1a1a3a",  # Deep purple glow
        pulse="#ff2a6d",  # Matching warning for alerts
    ),
    # Dracula Theme - Increased contrast
    "dracula": Theme(
        name="Dracula",
        background="#1e1f29",  # Darker background
        foreground="#ffffff",  # Pure white
        primary="#bd93f9",  # Soft purple (unchanged)
        secondary="#ff79c6",  # Vibrant pink (unchanged)
        highlight="#50fa7b",  # Lime green
        warning="#ff5555",  # Coral red
        glow="#44475a",  # Gray-purple
        pulse="#ffb86c",  # Orange
    ),
    # Nord Theme - Cooler tones with higher contrast
    "nord": Theme(
        name="Nord",
        background="#232933",  # Darker blue-gray
        foreground="#eceff4",  # Brighter text
        primary="#5e81ac",  # Deep nordic blue
        secondary="#b48ead",  # Lilac purple
        highlight="#a3be8c",  # Sage green
        warning="#bf616a",  # Cranberry red
        glow="#3b4252",  # Darker blue-gray
        pulse="#d08770",  # Terracotta
    ),
    # Gruvbox Dark - Warmer, more saturated colors
    "gruvbox": Theme(
        name="Gruvbox Dark",
        background="#1d2021",  # Darker gray
        foreground="#fbf1c7",  # Brighter beige
        primary="#458588",  # Teal blue (unchanged)
        secondary="#b16286",  # Raspberry pink
        highlight="#98971a",  # Olive green
        warning="#fb4934",  # Bright vermilion
        glow="#3c3836",  # Darker gray
        pulse="#fabd2f",  # Golden yellow
    ),
    # Solarized Dark - Enhanced with deeper contrasts
    "solarized": Theme(
        name="Solarized Dark",
        background="#00212b",  # Deeper teal
        foreground="#93a1a1",  # Brighter gray-cyan
        primary="#268bd2",  # Azure blue
        secondary="#d33682",  # Magenta (replaces purple)
        highlight="#859900",  # Lime green
        warning="#dc322f",  # Fire engine red
        glow="#073642",  # Darker teal
        pulse="#cb4b16",  # Pumpkin orange
    ),
    # Tokyo Night - More vibrant night colors
    "tokyo": Theme(
        name="Tokyo Night",
        background="#16161e",  # Deeper blue-black
        foreground="#c0caf5",  # Brighter lavender
        primary="#7aa2f7",  # Bright azure (unchanged)
        secondary="#9d7cd8",  # Royal purple
        highlight="#9ece6a",  # Apple green
        warning="#f7768e",  # Watermelon pink
        glow="#2a2a3a",  # Brighter dark blue
        pulse="#ff9e64",  # Tangerine
    ),
    # NEW THEME: Deep Ocean
    "ocean": Theme(
        name="Deep Ocean",
        background="#001a33",  # Deep navy
        foreground="#b3e0ff",  # Light sky blue
        primary="#00b3b3",  # Turquoise
        secondary="#ff66b2",  # Bubblegum pink
        highlight="#66ff66",  # Electric green
        warning="#ff6600",  # Bright orange
        glow="#003366",  # Dark blue glow
        pulse="#ffcc00",  # Sun yellow
    ),
    # NEW THEME: Firewatch
    "firewatch": Theme(
        name="Firewatch",
        background="#1a1d2b",  # Deep indigo
        foreground="#f8f8f0",  # Cream white
        primary="#ff5e5b",  # Coral
        secondary="#ffca5f",  # Sunbeam yellow
        highlight="#5aff5f",  # Neon green
        warning="#ff2e63",  # Raspberry
        glow="#2b2d42",  # Dark purple-blue
        pulse="#ff9a00",  # Amber
    ),
# 1. Midnight Purple
    "midnight": Theme(
        name="Midnight Purple",
        background="#0a041a",
        foreground="#e0d4ff",
        primary="#9a77ff",
        secondary="#ff6ad5",
        highlight="#66ffcc",
        warning="#ff6b6b",
        glow="#1a0f35",
        pulse="#ffb86c"
    ),
    
    # 2. Forest Deep
    "forest": Theme(
        name="Forest Deep",
        background="#0c1a0f",
        foreground="#d8ebd6",
        primary="#4caf50",
        secondary="#ff9800",
        highlight="#8bc34a",
        warning="#f44336",
        glow="#1a2a1c",
        pulse="#ffeb3b"
    ),
    
    # 3. Sunset Dunes
    "dunes": Theme(
        name="Sunset Dunes",
        background="#2a1503",
        foreground="#ffe0c2",
        primary="#ff6b35",
        secondary="#00a8cc",
        highlight="#ffd166",
        warning="#ef476f",
        glow="#3a2513",

        pulse="#ff9e00"
    ),
    
    # 4. Arctic Ice
    "arctic": Theme(
        name="Arctic Ice",
        background="#001f3f",
        foreground="#e6f7ff",
        primary="#00b4d8",
        secondary="#ff70a6",
        highlight="#90e0ef",
        warning="#ff4d6d",
        glow="#002b4f",
        pulse="#ffea00"
    ),
    
    # 5. Candy Rush
    "candy": Theme(
        name="Candy Rush",
        background="#1a001a",
        foreground="#ffd6ff",
        primary="#ff6ec7",
        secondary="#6effb4",
        highlight="#ffcc66",
        warning="#ff3366",
        glow="#2a002a",
        pulse="#ff00ff"
    ),
    
    # 6. Matrix Green
    "matrix": Theme(
        name="Matrix Green",
        background="#001100",
        foreground="#00ff41",
        primary="#00cc66",
        secondary="#ff003c",
        highlight="#39ff14",
        warning="#ff5500",
        glow="#002200",
        pulse="#00ffbf"
    ),
    
    # 7. Royal Gold
    "royal": Theme(
        name="Royal Gold",
        background="#1a0d00",
        foreground="#ffd700",
        primary="#d4af37",
        secondary="#c0c0c0",
        highlight="#ffdf00",
        warning="#ff4136",
        glow="#2a1a00",
        pulse="#ff8c00"
    ),
    
    # 8. Deep Space
    "space": Theme(
        name="Deep Space",
        background="#000022",
        foreground="#aaccff",
        primary="#5e60ce",
        secondary="#ff6b6b",
        highlight="#64dfdf",
        warning="#ff2e63",
        glow="#0a0a3a",
        pulse="#ff9e00"
    ),
    
    # 9. Cherry Blossom
    "cherry": Theme(
        name="Cherry Blossom",
        background="#1a000d",
        foreground="#ffd6e7",
        primary="#ff85a2",
        secondary="#ffd166",
        highlight="#ff6b6b",
        warning="#ff2e63",
        glow="#2a001a",
        pulse="#ff007f"
    ),
    
    # 10. Ocean Depths
    "abyss": Theme(
        name="Ocean Depths",
        background="#000d1a",
        foreground="#aaffff",
        primary="#0077be",
        secondary="#ff6b6b",
        highlight="#00ccbb",
        warning="#ff4136",
        glow="#001a2a",
        pulse="#00ffff"
    ),
    
    # 11. Desert Mirage
    "mirage": Theme(
        name="Desert Mirage",
        background="#2a1503",
        foreground="#ffe0c2",
        primary="#ff9a3c",
        secondary="#5dade2",
        highlight="#ffd166",
        warning="#e74c3c",
        glow="#3a2513",
        pulse="#f39c12"
    ),
    
    # 12. Neon Jungle
    "jungle": Theme(
        name="Neon Jungle",
        background="#001a0d",
        foreground="#ccffcc",
        primary="#39ff14",
        secondary="#ff00ff",
        highlight="#00ffcc",
        warning="#ff003c",
        glow="#002a1a",
        pulse="#ffcc00"
    ),
    
    # 13. Vintage Sepia
    "vintage": Theme(
        name="Vintage Sepia",
        background="#1a1200",
        foreground="#e8d8b6",
        primary="#c19a6b",
        secondary="#8a9a5b",
        highlight="#d4b483",
        warning="#d9534f",
        glow="#2a1e00",
        pulse="#d4af37"
    ),
    
    # 14. Cyber Void
    "void": Theme(
        name="Cyber Void",
        background="#000000",
        foreground="#00ffff",
        primary="#ff00ff",
        secondary="#00ff00",
        highlight="#ff5500",
        warning="#ff003c",
        glow="#0a0a0a",
        pulse="#ffcc00"
    ),
    
    # 15. Lavender Mist
    "lavender": Theme(
        name="Lavender Mist",
        background="#0d061a",
        foreground="#e6e6ff",
        primary="#9b5de5",
        secondary="#f15bb5",
        highlight="#00bbf9",
        warning="#ff6b6b",
        glow="#1a0f2a",
        pulse="#fee440"
    ),
    
    # 16. Blood Moon
    "bloodmoon": Theme(
        name="Blood Moon",
        background="#1a0000",
        foreground="#ffcccc",
        primary="#ff3333",
        secondary="#ff9933",
        highlight="#ff6666",
        warning="#ff0033",
        glow="#2a0000",
        pulse="#ff5500"
    ),
    
    # 17. Glacier Blue
    "glacier": Theme(
        name="Glacier Blue",
        background="#001a33",
        foreground="#e6f7ff",
        primary="#66b3ff",
        secondary="#ff99cc",
        highlight="#80dfff",
        warning="#ff6666",

        glow="#002b4d",
        pulse="#00ccff"
    ),
    
    # 18. Amber Waves
    "amber": Theme(
        name="Amber Waves",
        background="#1a0d00",
        foreground="#ffd9b3",
        primary="#ff9933",
        secondary="#66ccff",
        highlight="#ffcc66",
        warning="#ff3333",
        glow="#2a1a00",
        pulse="#ffcc00"
    ),
    
    # 19. Emerald City
    "emerald": Theme(
        name="Emerald City",
        background="#001a0a",
        foreground="#d9ffd9",
        primary="#00cc66",
        secondary="#ff66b2",
        highlight="#66ff99",
        warning="#ff3333",
        glow="#002a1a",
        pulse="#00ff99"
    ),
    
    # 20. Sunset Horizon
    "horizon": Theme(
        name="Sunset Horizon",
        background="#1a001a",
        foreground="#ffd6ff",
        primary="#ff6ec7",
        secondary="#ffcc00",
        highlight="#ff9933",
        warning="#ff3366",
        glow="#2a002a",
        pulse="#ff00cc"
    ),   
    # Interstellar Theme - Based on deep space colors with purple/blue tones
    "interstellar": Theme(
        name="Interstellar",
        background="#0b0916",  # ebony - deep space black
        foreground="#bdbfe1",  # periwinkle-gray - soft lavender text
        primary="#5763af",     # blue-violet - main accent
        secondary="#7c92d6",   # chetwode-blue - brighter blue
        highlight="#8d5261",   # au-chico - muted pink for highlights
        warning="#ff6666",    # Added a warning red for better visibility
        glow="#1d1c45",       # port-gore - dark blue glow
        pulse="#5763af",      # blue-violet - matching primary for pulses
    ),
    # ===== Popular Light Themes =====
    # Solarized Light - Classic light theme
    "solarized_light": Theme(
        name="Solarized Light",
        background="#fdf6e3",
        foreground="#586e75",
        primary="#268bd2",
        secondary="#d33682",
        highlight="#859900",
        warning="#dc322f",
        glow="#eee8d5",
        pulse="#cb4b16"
    ),

    # Gruvbox Light - Warmer light variant
    "gruvbox_light": Theme(
        name="Gruvbox Light",
        background="#fbf1c7",
        foreground="#3c3836",
        primary="#458588",
        secondary="#b16286",
        highlight="#98971a",
        warning="#cc241d",
        glow="#ebdbb2",
        pulse="#d79921"
    ),

    # Nord Light - Cool nordic light theme
    "nord_light": Theme(
        name="Nord Light",
        background="#eceff4",
        foreground="#2e3440",
        primary="#5e81ac",
        secondary="#b48ead",
        highlight="#a3be8c",
        warning="#bf616a",
        glow="#e5e9f0",
        pulse="#d08770"
    ),

    # One Light - Popular Atom editor theme
    "one_light": Theme(
        name="One Light",
        background="#fafafa",
        foreground="#383a42",
        primary="#4078f2",
        secondary="#a626a4",
        highlight="#50a14f",
        warning="#e45649",
        glow="#f0f0f0",
        pulse="#c18401"
    ),

    # GitHub Light - Official GitHub theme
    "github_light": Theme(
        name="GitHub Light",
        background="#ffffff",
        foreground="#24292e",
        primary="#0366d6",
        secondary="#6f42c1",
        highlight="#22863a",
        warning="#d73a49",
        glow="#f6f8fa",
        pulse="#d15704"
    ),

    # Material Light - Google's material design
    "material_light": Theme(
        name="Material Light",
        background="#fafafa",
        foreground="#212121",
        primary="#3f51b5",
        secondary="#ff4081",
        highlight="#4caf50",
        warning="#ff5252",
        glow="#f5f5f5",
        pulse="#ff9800"
    ),

    # Paper Light - Clean minimal theme
    "paper": Theme(
        name="Paper Light",
        background="#eeeeee",
        foreground="#212121",
        primary="#00bcd4",
        secondary="#ff4081",
        highlight="#4caf50",
        warning="#ff5722",
        glow="#f5f5f5",
        pulse="#ffc107"
    ),

    # Everforest Light - Soft natural colors
    "everforest_light": Theme(
        name="Everforest Light",
        background="#f7f2df",
        foreground="#5c6a72",
        primary="#8da101",
        secondary="#df69ba",
        highlight="#3a94c5",
        warning="#f85552",
        glow="#efebc0",
        pulse="#dfa000"
    ),

    # Catppuccin Latte - Popular light variant
    "catppuccin_latte": Theme(
        name="Catppuccin Latte",
        background="#eff1f5",
        foreground="#4c4f69",
        primary="#1e66f5",
        secondary="#ea76cb",
        highlight="#40a02b",
        warning="#d20f39",
        glow="#e6e9ef",
        pulse="#df8e1d"
    ),

    # Rosé Pine Dawn - Gentle muted theme
    "rose_dawn": Theme(
        name="Rosé Pine Dawn",
        background="#faf4ed",
        foreground="#575279",
        primary="#286983",
        secondary="#d7827e",
        highlight="#56949f",
        warning="#b4637a",
        glow="#f2e9e1",
        pulse="#ea9d34"
    ),

    # Tokyo Day Light - Bright vibrant theme
    "tokyo_day": Theme(
        name="Tokyo Day",
        background="#e1e2e7",
        foreground="#4a4b6a",
        primary="#2e7de9",
        secondary="#9854f1",
        highlight="#587539",
        warning="#f52a65",
        glow="#d7d8dc",
        pulse="#8c6c3e"
    ),

    # Horizon Light - Modern pastel theme
    "horizon_light": Theme(
        name="Horizon Light",
        background="#fdf0ed",
        foreground="#403c3d",
        primary="#da103f",
        secondary="#1d8991",
        highlight="#edb8ac",
        warning="#e95678",
        glow="#fadad1",
        pulse="#f09383"
    ),

    # Ayu Light - Clean developer theme
    "ayu_light": Theme(
        name="Ayu Light",
        background="#fafafa",
        foreground="#5c6773",
        primary="#ff9940",
        secondary="#59c2ff",
        highlight="#86b300",
        warning="#f07178",
        glow="#f0f0f0",
        pulse="#a37acc"
    ),

    # GitHub Dark Dimmed - Light-medium contrast
    "github_dimmed": Theme(
        name="GitHub Dimmed",
        background="#22272e",
        foreground="#adbac7",
        primary="#539bf5",
        secondary="#b083f0",
        highlight="#57ab5a",
        warning="#e5534b",
        glow="#2d333b",
        pulse="#daaa3f"
    ),

    # Summer Pop - Vibrant summer colors
    "summer": Theme(
        name="Summer Pop",
        background="#fff9e6",
        foreground="#3a405f",
        primary="#ff6e6e",
        secondary="#5e81ac",
        highlight="#88c0d0",
        warning="#bf616a",
        glow="#ffefcf",
        pulse="#ebcb8b"
    ),

    # Frost - Cool blue-based theme
    "frost": Theme(
        name="Frost Light",
        background="#edf2f7",
        foreground="#2d3748",
        primary="#3182ce",
        secondary="#9f7aea",
        highlight="#38a169",
        warning="#e53e3e",
        glow="#e2e8f0",
        pulse="#dd6b20"
    ),

    # Espresso - Coffee-inspired theme
    "espresso": Theme(
        name="Espresso Light",
        background="#e8e1d1",
        foreground="#4a3a2b",
        primary="#c45d4c",
        secondary="#7a9f8e",
        highlight="#8a9b69",
        warning="#c44f3a",
        glow="#d8d0be",
        pulse="#b88a5e"
    ),

    # Zenburn Light - Low-contrast comfortable theme
    "zenburn_light": Theme(
        name="Zenburn Light",
        background="#f0f0e6",
        foreground="#4f4f4f",
        primary="#7f9f7f",
        secondary="#dc8cc3",
        highlight="#8cd0d3",
        warning="#cc9393",
        glow="#e6e0cc",
        pulse="#e3ceab"
    ),

    # Breeze Light - KDE default theme
    "breeze": Theme(
        name="Breeze Light",
        background="#fcfcfc",
        foreground="#232627",
        primary="#2980b9",
        secondary="#9b59b6",
        highlight="#27ae60",
        warning="#da4453",
        glow="#eff0f1",
        pulse="#f67400"
    ),

    # Google Light - Material design colors
    "google_light": Theme(
        name="Google Light",
        background="#ffffff",
        foreground="#202124",
        primary="#1a73e8",
        secondary="#ea4335",
        highlight="#34a853",
        warning="#fbbc04",
        glow="#f8f9fa",
        pulse="#fa7b17"
    )

}
