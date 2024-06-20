import py_compile
import os

os.system("cls")

print("""
the most basic .py to .pyc converter ever
------------------------------------------
commands:
    compile
    help
    about
    quit
    clear
""")

while True:
    ask = input()
    if ask == "compile":
        file = input("what file do you want to be compiled to bytecode (include extension and/or path): ")
        if os.path.isfile(file):
            py_compile.compile(file)
        else:
            print("the file entered was not a real file try again")
    if ask == "help":
        print("""
compile - compiles written python code into bytecode
quit - quits the program
clear - resets the CLI       
    """)
    if ask == "about":
        print("made by UPGSOFTWARE a division of WIZARD STUDIOS, copyleft MMXXIV, some rights reserved")
    if ask == "quit":
        quit()
    if ask == "clear":
        os.system("cls")
        print("""
the most basic .py to .pyc converter ever
------------------------------------------
commands:
    compile
    help
    about
    quit
    clear
    """)