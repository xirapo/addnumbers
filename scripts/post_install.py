import pathlib, os, sys, shutil

current_path =pathlib.Path(__file__).parent.absolute()
RESOLVER_DIR_NAME ='addnumbers'
FILES_TO_MOVE =['main.py', '__init__.py']

def install():
    resolver_path = sys.argv[1]
    print("Running Post Install...")
    current = os.path.split(current_path)
    path = os.path.join(current[0],RESOLVER_DIR_NAME)
    print(f"copy files from: {path}")
    print(f"to new path {resolver_path}")
    list_of_files = os.listdir(path)
    for roots,dirs,files in os.walk(path):
        for f in files:
            if  f in FILES_TO_MOVE:
                print(f)
                shutil.copy(f,resolver_path)


install()