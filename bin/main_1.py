import read_envato_license
import impfunc
from colorama import Fore,Style
### Main Program Now
## Print main menu

def main():

    #calls menu input
    print(Style.RESET_ALL)
    menuInput()

def menu():
        print(Fore.YELLOW +'''______________________________________________________________________________________________________________________________
||||||||||||||||||||||||||||||||||||         PROGRAM BROUGHT TO YOU BY AMIT GUPTA         ||||||||||||||||||||||||||||||||||||''')
    
        print(Fore.WHITE +'''
    ______________________________________________________________________________________________________________
    ******************** This Program to Help you extract licenses from Envato Elements Files ********************
    ______________________________________________________________________________________________________________
    Select option to choose:
            1. Fixed Folder                                 ....[1]
            2. Choose Dynamic Folder                        ....[2]
            3. Exit                                         ....[3]
    ______________________________________________________________________________________________________________
    ''')


def menuInput():
    while True:
        menu()
        choice = impfunc.numInput("choice")
    
        if choice==1:
            typec=impfunc.output_format()
            x=read_envato_license.menuchosen_v1(typec)
            print(x)
            # break
        elif choice == 2:
            typec=impfunc.output_format()
            x=read_envato_license.menuchosen_v2(typec)
            print(x)
            # break
        elif choice ==3:
            print("Thanks for using this program Bye Bye !!!")
            exit()
        else:
            print(Fore.RED +'Try again ')

#Calls main
main()

