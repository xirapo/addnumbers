import pathlib

current =pathlib.Path(__file__).parent.absolute()
def install(self):
    print("Running Post Install...")
    print(current)
    return self