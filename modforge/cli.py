import argparse
from make import make_dependencies
from handle_module import (track, init, delete, untrack)
from watcher import watch
import os


def print_success(sg):
    print(sg)

def print_error(sg):
    print(sg)

def main():

    
    parser = argparse.ArgumentParser(prog='modforge')
    subparsers = parser.add_subparsers()

    track_parser = subparsers.add_parser('track')
    track_parser.set_defaults(func=track)
    track_parser.add_argument("project")
    track_parser.add_argument("module")
    track_parser.add_argument("level", default=0)
    
    
    untrack_parser = subparsers.add_parser('untrack')
    untrack_parser.set_defaults(func=untrack)
    untrack_parser.add_argument("project")
    untrack_parser.add_argument("module")
    

    init_parser = subparsers.add_parser('init')
    init_parser.set_defaults(func=init)
    init_parser.add_argument("project")
    init_parser.add_argument("-path", "-p" , default=os.getcwd())
    
    delete_parser = subparsers.add_parser('delete')
    delete_parser.set_defaults(func=delete)
    delete_parser.add_argument("project")

    add_parser = subparsers.add_parser('make')
    add_parser.set_defaults(func=make_dependencies)
    add_parser.add_argument("project")
    
    
    watch_parser = subparsers.add_parser('watch')
    watch_parser.set_defaults(func=watch)
    watch_parser.add_argument("project")
    
    args = vars(parser.parse_args())
    print(args)
    if 'func' in args:
        args.pop('func')(**args)
    else:
        parser.print_usage()
        return
    

if __name__ == "__main__":
    main()