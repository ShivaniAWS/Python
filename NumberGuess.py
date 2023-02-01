#This is a simple Python program for Number guessing.
import random

while(1):
    try:
        input_range = int(input("Enter end range "))

    except:
        print("Not a valid int")
        continue
    break
rand_number = random.randint(0, input_range)
guess = 0
while(1):

        try :
            input_number = int(input("Guess the number "))
        except:
            print("Enter valid int")
            guess+=1
            continue
        if(rand_number == input_number) :
            print("Correct!!")
            break
        else :
            print("Wrong!!, Try again ")
            guess+=1
            continue
print("You got",guess,"wrong guesses")




