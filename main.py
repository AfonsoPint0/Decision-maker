import os
import random

option = []

# Add options
def add():
    while True:
        var = input(r"Insert one option or type '/quit' to exit"+"\n\t")
        if var != r"/quit":
            option.append(var)
        else:    
            menu()

# Check options
def check():
    if(len(option) >= 1):
        for i in range(len(option)):
            print("Option " + str(i) + " : " + option[i] + "\n")
        os.system('pause')
    else:
        print("\tThe list of options is empty\n")
        os.system('pause')
    menu()

# Chose random option
def randomize():
    if(len(option) >= 1):
        random_option = random.choice(option)
        print("Choice : " + random_option + "\n")
        os.system('pause')
    else:
        print("\tThe list of options is empty\n")
        os.system('pause')
    menu()

# Clear options
def clear():
    option.clear()
    print("Options have been cleared\n")
    os.system('pause')
    menu()

# Close app
def close():
    print("\n\tBye\n")
    exit()

# Invalid choice
def error():
    print("\n\tInvalid choice\n\t")    
    os.system('pause')
    menu()

# Main menu
def menu():
    os.system('cls')
    print("""
    Decision maker
    --------------------                                                             
            MENU
    --------------------                                                             
    1   Add option
    2   Check options
    3   Get random option
    4   Clear options
    0   Exit
    --------------------
    """)
    choice = input("\tChoice : ")

    if choice == "1" :
        add()

    elif choice == "2" :
        check()

    elif choice == "3" : 
        randomize()

    elif choice == "4" : 
        clear()

    #Exit
    elif choice == "0" or choice == "exit" or choice == "quit" :
        close()
    
    #Invalid choice 
    else:
        error()
        
menu()
