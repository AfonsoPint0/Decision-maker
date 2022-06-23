import os

option = []

# Add options
def add():
    while True:
        var = input(r"Insert one word or type '/quit' to exit")
        if var == r"/quit":
            intro()
        option.append(var)
            
    

# Main menu
def intro():
    os.system('cls')
    print("""
    MENU
    --------------------                                                             
    1   Add option
    2   Clear options
    3   Randomize
    0   Exit
    --------------------
    """)
    var= input("\tChoice : ")

    if var == "1" :
        add()

    elif var == "2" : 
        print("nada")

    #Exit
    elif var == "0" or var == "exit" or var == "quit" :
        exit("\tBye\n")
    
    #Invalid choice 
    else:
        print("\n\tInvalid choice\n")
        
        os.system('pause')    
        intro()

    

add()
