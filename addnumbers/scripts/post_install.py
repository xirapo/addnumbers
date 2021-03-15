import pathlib, os, sys, shutil

current =pathlib.Path(__file__).parent.absolute()
list_of_files =os.listdir(current)

def install():
    pth = sys.argv[1]
    print("Running Post Install...")
    print(f"new folder path: {pth}")
    for root, dirs, files in os.walk(current):
        for f in files:
            if f.endswith('.py'):
                shutil.copy(os.path.join(root,f),pth)