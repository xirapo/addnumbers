import pathlib, os

current =pathlib.Path(__file__).parent.absolute()
files =os.listdir(current)
def install(pth):
    print("Running Post Install...")
    print(f"new folder path: {pth}")
    for f in files:
        print(f)