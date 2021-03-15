import pathlib, os

current =pathlib.Path(__file__).parent.absolute()
files =os.listdir(current)
def install():
    print("Running Post Install...")
    return files