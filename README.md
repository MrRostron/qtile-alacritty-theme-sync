# Qtile-Alacritty Theme Sync
Sync Alacritty terminal colors with your Qtile theme automatically

## Features
- 30+ preconfigured themes
- Automatic theme detection
- Preserves existing Alacritty settings
- One-command installation

## Installation
```bash
git clone https://github.com/MrRostron/qtile-alacritty-theme-sync.git
cd qtile-alacritty-theme-sync
paru -S python-toml

# Copy files to config directories
cp sync_alac/themes.py ~/.config/qtile/
cp sync_alac/sync_alacritty.py ~/.config/qtile/
# make script executable
chmod +x ~/.config/qtile/sync_alacritty.py
```

```python
# In ~/.config/qtile/config.py add the following lines towards the top of your config.
import os
import subprocess
from themes import Theme

theme = Theme.get_theme("Gruvbox")  # Change theme name

# Add theme detection Hook towards the end of your config file.
# Add this to hooks section
@hook.subscribe.startup
def sync_alacritty_theme():
    subprocess.Popen([os.path.expanduser("~/.config/qtile/sync_alacritty.py")])
```

### Modify Paths in `sync_alacritty.py` and `themes.py`
```python
# Change to user's config location
ALACRITTY_CONFIG = os.path.expanduser("~/.config/alacritty/alacritty.toml")
QTILE_CONFIG = os.path.expanduser("~/.config/qtile/config.py")
```





