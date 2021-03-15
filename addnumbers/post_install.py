import pathlib, os, sys

current =pathlib.Path(__file__).parent.absolute()
files =os.listdir(current)

def install():
    pth = sys.argv[1]
    print("Running Post Install...")
    print(f"new folder path: {pth}")
    for f in files:
        if f.endswith('.py'):
            print(f)