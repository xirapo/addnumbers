import pathlib, os, sys, shutil

current =pathlib.Path(__file__).parent.absolute()
list_of_files =os.listdir(current)
FILES_TO_BE_MOVE = [
    '__init__.py',
    'main.py'
]

def install():
    pth = sys.argv[1]
    print("Running Post Install...")
    print(f"new folder path: {pth}")
    for f in list_of_files:
        print(f)

