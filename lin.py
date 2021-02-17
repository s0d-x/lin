# Basic (Will give the "structure" e.g.: "nt", "posix")
#import os
#print(os.name)

# Detailed (Will give exact OS name)
#import platform
#print(platform.system())

import platform

osname = platform.system()

while True:

    usrin = input("> ")

    if usrin == "exit" or usrin == "quit":
        break

    elif usrin == "os.name":
        print(osname)

    else:
        print(usrin + ": Unknown command")
