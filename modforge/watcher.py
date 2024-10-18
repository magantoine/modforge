import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


from handle_module import load_cache
from make import make_dependencies


class Watcher:

    def __init__(self, project):
        self.observer = Observer()
        self.project = project

        self.dir_to_watch = load_cache(project)["dir_path"]



    def run(self):
        event_handler = Handler(self.project)
        self.observer.schedule(event_handler, self.dir_to_watch, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(10)
        except:
            self.observer.stop()
            print("Error")
        
        self.observer.join()


class Handler(FileSystemEventHandler):

    def __init__(self,
                 project:str) -> None:
        super().__init__()
        self.project = project

        

    # @staticmethod
    def on_any_event(self, event):
        if event.is_directory:
            return None

        elif event.event_type in ['modified', 'created']:
            if("__pycache__" not in event.src_path 
               and"__init__.py" not in event.src_path 
               and ".py" in event.src_path):
                
                print(f"Received {event.event_type} event - %s." % event.src_path)
                print("> Rebuild :")
                make_dependencies(self.project)



def watch(project):
    w = Watcher(project)
    w.run()
