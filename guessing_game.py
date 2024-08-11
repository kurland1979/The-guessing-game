#משחק הנחושים
#פונקציה פתיח עבור משחק
def Greetings_and_instructions():
    print("Welcome to Guess the Guesses! ")
    print()
    print("You must choose a number between 1 and 100")
    print()
    print("Let's see you succeed! ")
    print()

#הגדרת תווכים
def Defining_number_ranges(number):

    while True:
        if 1 <= number <= 100:
           return True
           
        else:
           print("Error: Please enter a valid number between 1 and 100.")
           return False
         
       

import random   

#בחירת מספר אקרעי
def Picking_a_random_number():
     num = random.randint(1,100) 

     return num


    #שאלה למשתמש אם הוא רוצה רמז
def The_clue_question(num, user_num):

    while True:
        choice = input("Would you like a hint for the number you selected,you can choose y or n: ")

        if choice == "n":
         break
       
        elif choice == "y":
          print( Hints_to_the_user(num, user_num))
        else:
          print("Invalid selection Please select y or n: ")
         

    return choice
          
    #פונקצית רמזים
def Hints_to_the_user(number_to_guess, user_guess):
    difference = abs(number_to_guess - user_guess)

    difference = abs(number_to_guess - user_guess)

    if 1 <= difference <= 5:
       return "Very hot"
    elif 6 <= difference <= 10:
       return "Hot"
    elif 11 <= difference <= 15:
       return "Cold"
    else:
       return "Very cold"
    

#פלט מהמשתמש עבור מספר שהוא רוצה להזין
def Receiving_a_number_from_the_user():
    while True:
        try:
          
            user_input = input("Enter your choice between 1 - 100: ")
            user_num = int(user_input)
            
           
            if 1 <= user_num <= 100:
                return user_num
            else:
                print("Error: Please enter a valid number between 1 and 100.")

        except ValueError:
            print("Error: Please enter a valid number.")

          
 #סיום משחק
def game_over():
    print("Game Over! Thank you for playing! ")
    

    while True:
      answer = input(" Do you want to keep guessing? y/n? ").strip().lower() 

      if answer == "n":
        print("Thanks for playing! Goodbye.")
        break

      elif answer == "y": 
        
        The_guessing_game()

        break

      else:
          print("Invalid answer, please try again: y/n:")
      
       
#פונקציה ראשית
def The_guessing_game():
    Greetings_and_instructions()
    num = Picking_a_random_number()
   

    while True:
        user_num  =  Receiving_a_number_from_the_user()

        if user_num == num:
          print(f"Congratulations! You've guessed the correct number: {num}")
          game_over()

          break
        else:
           The_clue_question(num,user_num)
           
          
      
if __name__ == "__main__":
         The_guessing_game()