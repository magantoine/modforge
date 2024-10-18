import os
import json

LEVELS = {
    "0": "TOP", 
    "1": "BOTTOM"
}
MODFORGE_DIR = "/Users/antoinemagron/Documents/PERSO/modforge/"

def load_cache(project):
    cache_file = os.path.join(MODFORGE_DIR, f".mods/{project}/{project}.json")
    with open(cache_file, "r") as cf:
        project_spec = json.load(cf)
    return project_spec


def write_cache(project, content):
    cache_file = os.path.join(MODFORGE_DIR, f".mods/{project}/{project}.json")
    with open(cache_file, "w") as cf:
        json.dump(content, cf)



def track(project, module, level):
    ## TODO IMPLEMENT PACKAGE REGISTERY HERE
    ## puts the dir structure in the dependencies.sh and the module in watcher

    ## 1) Check the folder exists
    project_spec = load_cache(project)

    print(project_spec)
    
    if(module in project_spec):
        raise ValueError(f"** Module {module} already registered for {project}")


    mod_path = os.path.join(project_spec["dir_path"], module.replace(".", "/"))

    print(">"*30, mod_path, "<"*30)
    
    if(not os.path.exists(mod_path)):
        raise ValueError(f"** Module {module} has no associated folder **")
    

    subfiles = [f for f in os.listdir(mod_path) if ".py" in f and "__init__" not in f]
    depfile_snip = "\n".join(f"from .{f.replace('.py', '')} import *" for f in subfiles)

    print(depfile_snip)
    
    project_spec[module] = {
        "path": mod_path,
        "level": LEVELS[level],
        "depfile_snip": depfile_snip,
        "name": module
    }
    ### WRITE IT OUT
    write_cache(project, project_spec)

    
    
def untrack(project, module):
    ## TODO IMPLEMENT PACKAGE REGISTERY HERE
    ## puts the dir structure in the dependencies.sh and the module in watcher

    ## 1) Check the folder exists
    project_spec = load_cache(project)
    
    if(module not in project_spec):
        raise ValueError(f"** Module {module} not registered for {project}")

    del project_spec[module]
    write_cache(project, project_spec)
    


def init(project, path):
    cache_specific_dir = os.path.join(MODFORGE_DIR, f".mods/{project}")
    os.mkdir(cache_specific_dir)
    cache_file = os.path.join(cache_specific_dir, f"{project}.json")
    if(os.path.exists(cache_file)):
        raise ValueError(f"** Project {project} already exists **")
    else :
        with open(cache_file, "w") as cf:
            json.dump({
                "dir_path": path,
                "project": project,
            }, cf)
        print(f"** Project {project} inited **")


def delete(project):
    cache_file = f".mods/{project}/{project}.json"
    if(not os.path.exists(cache_file)):
        raise ValueError(f"** Project {project} doesn't exists **")
    else:
        os.remove(cache_file)
        os.rmdir(f".mods/{project}")
        print(f"** Project {project} deleted **")


