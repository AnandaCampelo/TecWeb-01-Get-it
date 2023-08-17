import json
from pathlib import Path

def extract_route(route):
    return route.replace('HTTP', '/').split(' ')[1][1:]

def read_file(file):
    with open(file, 'r') as f:
        return f.read()
    
def load_data(file):
    data_path = Path('data') / file
    return json.loads(read_file(data_path))

def load_template(file):
    template_path = Path('templates') / file
    return read_file(template_path)