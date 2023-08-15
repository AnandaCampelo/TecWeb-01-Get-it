def extract_route(route):
    return route.replace('HTTP', '/').split(' ')[1][1:]

def read_file(file):
    with open(file, 'r') as f:
        return f.read()