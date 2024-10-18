## Decorator to manage dependencies
def expose(f):
    f.exposed = True
    return f