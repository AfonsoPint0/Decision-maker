import os

option = []

def intro():
    os.system('cls')
    print("""
    MENU
    -----------------------------------------------------------------------                                                             
    1   Add option
    2   Clear options
    3   Randomize
    0   Exit
    -----------------------------------------------------------------------
    """)
    var= input("\tChoice : ")

    if var == "1" :
        print(1)

        os.system('pause')    
        intro()
        
    #Exit
    elif var == "0" :
        exit("\tBye\n")
    
    #Invalid choice 
    else:
        print("\n\tInvalid choice\n")
        
        os.system('pause')    
        intro()

    

intro()