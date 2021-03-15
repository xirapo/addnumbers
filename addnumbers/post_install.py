import pathlib

current =pathlib.Path(__file__).parent.absolute()
def install():
    print("Running Post Install...")
    return current