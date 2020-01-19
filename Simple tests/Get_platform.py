import platform

def main():
    message()

def message():
    print("this is python version {}".format(platform.python_version()))

if __name__ == "__main__": main()