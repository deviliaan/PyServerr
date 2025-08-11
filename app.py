import time
from config import Config

# Config Parser Class
# Initialize the Config object
config = Config()

# Last run time
config.add('Settings', 'last_run', time.strftime('%Y-%m-%d %H:%M:%S'))









