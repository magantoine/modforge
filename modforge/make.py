import os
import sys
## TODO CHANGE
DIR_PATH = "/Users/antoinemagron/Documents/EPFL/PDM/crchum/"
TOP, BOTTOM = "TOP", "BOTTOM"

from handle_module import load_cache


## TODO CLEAN
def make_module(modn, level):
    __init__ = """"""
    print(f"> making module {modn}")
    mod = __import__(modn)

    ## for nested module 
    short_module = modn
    if(level == BOTTOM):
        short_module = modn.split(".")[-1]
    template = "from {module} import {object}\n"
    print(dir(mod))
    for f in dir(mod):
        cont = None
        if("dict" in str(type(mod.__dict__[f]))):
            cont = dict(mod.__dict__[f])
        elif(hasattr(mod.__dict__[f], "__dict__") or "dict" in str(type(mod))):
            cont = dict(mod.__dict__[f].__dict__)
        else :
            pass
        if(cont is not None and "exposed" in cont):
            complete_module = mod.__dict__[f].__module__
            object = mod.__dict__[f].__name__
            ## we don't add if comming from top module :
            if(short_module in complete_module):
                if(not (level == TOP and complete_module.count(".") > 1)):
                    __init__+=(
                        template.format(
                            module=complete_module.replace(modn, ""),
                            object=object
                            )
                        )
    print("_"*100)
    print(modn)    
    print(__init__)

    with open(f"{modn.replace('.', '/')}/__init__.py", "w") as f:
        f.write(__init__)
    
    del mod

    
def prepare_mod(mod):
    init_file = os.path.join(mod["path"], "__init__.py")
    os.remove(init_file)
    with open(init_file, "w") as f:
        f.write(mod["depfile_snip"])
    print(f"Prepared mod {mod['name']}")

def make_dependencies(project):
    modules = load_cache(project)
    dir_path = modules.pop("dir_path")
    os.chdir(dir_path)
    sys.path.append(dir_path)
    project = modules.pop("project")
    [prepare_mod(mod) for (_, mod)  in modules.items()]
    [make_module(modn, mod["level"]) for (modn, mod)  in modules.items()]





    # for modn, level in MODULES:
    
if __name__ == "__main__":
    make_dependencies()
    