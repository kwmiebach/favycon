import json
from jinja2 import Environment, FileSystemLoader

# Load the colors from the JSON file
with open('color.json', 'r') as f:
    json_content = json.load(f)

colors = json_content['colorlist']

# Set up the Jinja environment and template loader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render the HTML template with the loaded colors
html_content = template.render(colors=colors)

# Write the rendered content to the index.html file
with open('index.html', 'w') as f:
    f.write(html_content)
    