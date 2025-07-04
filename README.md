# Qtile-Alacritty Theme Sync
Sync Alacritty terminal colors with your Qtile theme automatically. themes.py serves as the centralized colour theme management across the Qtile configuration. It provides color data to bars/widgets/layouts and will sync these to Alacritty. An example of the configuration is included in sample_config/

## Features
- 30+ preconfigured themes
- Automatic theme detection
- Preserves existing Alacritty settings
![git1](https://github.com/user-attachments/assets/a4ae62ea-1d33-4e1e-96af-93d86f2eb80b)
![git2](https://github.com/user-attachments/assets/ceb36107-0044-4706-b043-2a5ee316ac1c)

## Installation
```bash
git clone https://github.com/MrRostron/qtile-alacritty-theme-sync.git
cd qtile-alacritty-theme-sync
```
```bash
# we need the toml python package
pip install toml
```
```bash
# Arch Linux
sudo pacman -S python-toml
```
```bash
# Copy files to config directories
cp sample_config/themes.py ~/.config/qtile/
cp sample_config/sync_alacritty.py ~/.config/qtile/
```
```bash
# make script executable
chmod +x ~/.config/qtile/sync_alacritty.py
```
## Post-Install Configuration

1. **Add to Qtile Config**:
```python
# Add to ~/.config/qtile/config.py
import os
import subprocess
from libqtile import hook
from themes import Theme

# ===== Colour Theme =====
theme = Theme.get_theme("Gruvbox") # Change theme name

#Theme colours
BACKGROUND = theme.background
FOREGROUND = them.foreground
PRIMARY = theme.primary
SECONDARY = theme.highlight
WARNING = theme.warning

# Add hooks to hook section towards end of your config
@hook.subscribe.startup
def sync_alacritty_theme():
    subprocess.Popen([os.path.expanduser("~/.config/qtile/sync_alacritty.py")])

@hook.subcribe.startup_once
def autostart():
subprocess.Popen([os.path.expanduser("~/.config/qtile/sync_alacritty.py")])
```
2. ** Modify Paths in `sync_alacritty.py` and `themes.py`

```python 
# Change to user's config location if needed
ALACRITTY_CONFIG = os.path.expanduser("~/.config/alacritty/alacritty.toml")
QTILE_CONFIG = os.path.expanduser("~/.config/qtile/config.py")A
```

3. **Test Configuration**
```bash
# Run manually to test
python ~/.config/qtile/sync_alacritty.py

# Should show:
# Updated Alacritty config with Gruvbox theme
```

## Adding New Themes
1. Edit `themes.py`
2. Add new entry to THEMES dictionary:
```python
"theme-name": Theme(
    name="Theme Name",
    background="#COLOR",
    foreground="#COLOR",
    primary="#COLOR",
    secondary="#COLOR",
    highlight="#COLOR",
    warning="#COLOR",
    glow="#COLOR",
    pulse="#COLOR"
),
```

4. **Example Usage**
```python
# Screens
layout.MonadTall(
    border_focus=PRIMARY,
    border_normal=SECONDARY,
)

# Widgets
widget.GroupBox(
    foreground=FOREGROUND,
    active=PRIMARY,
    inactive=SECONDARY,
    block_highlight_text_color=FOREGROUND,
    highlight_method="block",
    this_current_screen_border=HIGHLIGHT,
    borderwidth=1,
    padding_x=8,
    spacing=8,
    urgent_alert_method="block",
    urgent_text=ACCENT
)
```
![gra](https://github.com/user-attachments/assets/5394890d-ebc1-4543-84d1-0eaf0556731f)

    




