import time
from config import Config
from flask import Flask
# Config Parser Class
# Initialize the Config object
config = Config()

# Last run time
config.add('Settings', 'last_run', time.strftime('%Y-%m-%d %H:%M:%S'))

# Server configuration
config.add('Server','host','127.0.0.1')
config.add('Server','port','5000')


# Create Flask app
app = Flask(__name__)



# Load configuration from config.ini And Run the App
app.run(debug=True,host=config.get('Server', 'host'), port=int(config.get('Server', 'port')))



