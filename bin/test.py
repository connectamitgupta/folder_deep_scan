def main():
#calls menu input
  menuInput()

def menu():
#assigns the menu to menuDisplay
  menuDisplay = print('''
  Welcome! Please make a choice from the following menu

  1. Select a year and display available data
  2. Review averages by year range
  3. Select a date range to display highest
  4. Select a date range to display lowest 
  5. Get total for a selected year range
  6. blank
  7. blank
  8. See this menu again
  9. QUIT the program
''')


def menuInput():
#loops until 9 is selected  
    while True:
        menu()
        try:
            userChoice=int(input('Please make a selection: '))
        except ValueError:
            print('Please enter a whole number less than or equal to 9')

        if userChoice > 9:
            print('Please enter a number less or equal to 9')
        elif userChoice == 0:
            print('Please enter a number greater than 0')
        elif userChoice == 1:
            print('Good')
        elif userChoice == 2:
            print('Good')
        elif userChoice == 3:
            print('Good')
        elif userChoice == 4:
            print('Good')
        elif userChoice == 5:
            print('Good')
        elif userChoice == 6:
            print('Good')
        elif userChoice == 7:
            print('Invalid Choice')
        elif userChoice == 8:
            print('Good')
        else:
            print('Thank you! Program Exiting!')
            exit(1)

#Calls main 
main()