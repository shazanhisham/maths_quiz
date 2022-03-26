
import sys
import quick.Quick_game
import custom.easy
import custom.medium
import custom.hard
import past_record.Past_result
import past_record.Delete_result

#Creating Intoduction
title="****** Welcome to Math Quiz Game ******"
print("="*len(title))
print(title)
print("="*len(title))

while True:
    print("\n")
    print("1) Quick Game")
    print("2) Custom Game")
    print("3) Past Game details")
    print("4) Exit.")
    option = input("\nEnter your Option -> ")
    if option == "4":
        print("\n")
        print("."*len(title))
        break
    elif option == "1":
        print("\n")
        quick.Quick_game.Quick()
    elif option == "2":
        print("\nChoose the Difficulty Level from belows :")
        while True:
            print("\n ")
            print("a) Easy Level")
            print("b) Medium Level")
            print("c) Hard Level")
            print("d) Exit to main menu")
            option=input("\nEnter your option -> ")
            if option=="d":
                print("\n")
                print("."*len(title))
                break
            elif option=="a":
                print("\n")
                custom.easy.easy()
            elif option=="b":
                print("\n")
                custom.medium.medium()
            elif option=="c":
                print("\n")
                custom.hard.hard()
            else:
                print("\n")
                print("Incorrect choice... Try Again")
    elif option == "3":
        print("\nChoose your choice from belows :")
        while True:
            print("\n")
            print("a) View past player details")
            print("b) Delete all past player details")
            print("c) Return to Main menu")
            option=input("\n Enter your choice : ")
            if option=="c":
                print("\n")
                print("."*len(title))
                break
            elif option=="a":
                print("\n")
                past_record.Past_result.past_results()
            elif option=="b":
                print("\n")
                past_record.Delete_result.delete_results()
            else:
                print("\n")
                print("Incorrect Choice...Try Again")
    else:
        print("\n")
        print ("Incorrect choice... Try Again")
