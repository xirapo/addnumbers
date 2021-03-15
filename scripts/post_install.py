import pathlib, os, sys, shutil

current_path =pathlib.Path(__file__).parent.absolute()
RESOLVER_DIR_NAME ='addnumbers'

def install():
    resolver_path = sys.argv[1]
    print("Running Post Install...")
    print(f"new folder path: ")
    current = os.path.split(current_path)
    path = os.path.join(current[0],RESOLVER_DIR_NAME)
    print(f"copy files from: {path}")
    print(f"to new path {resolver_path}")
    list_of_files = os.listdir(path)
    for f in list_of_files:
        if f.endswith('.py'):
            shutil.copy(f,resolver_path)
            print(f"we are moving {f} to {resolver_path}")