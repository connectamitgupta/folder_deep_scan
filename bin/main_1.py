import read_envato_license
### Main Program Now
## Print main menu
while True:
    print('''
    ******** This Program to Help you extract licenses from Envato Elements Files
    Select option to choose:
            1. Fixed Folder
            2. Choose Dynamic Folder
            3. Exit
    ''')

    choice=int(input("*   "))

    if choice==1 or choice==2:
        print('''
        ******** What do you want to generate XLSX or CSV
        Select option to choose:
                1. XLSX
                2. Json
        ''')
        type=int(input("#   "))



    if choice==1:
        x=read_envato_license.menuchosen_v1()
        print("good",x)
        # break
    elif choice == 2:
        x=read_envato_license.menuchosen_v2()
        print("good",x)
        # break
    elif choice ==3:
        print("Bye Bye !!!")
        break
    else:
        print('Try again ')

    # print("Menu chosen by you is: ",choice)