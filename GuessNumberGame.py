import random 
import time
number = 0

def intro():
    global number 
    number = random.randint(1, 100)
    print("May I ask for your name? ")
    global name 
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")
    if (number %2 == 0):
        x = "even"
    else:
        x = "odd"
    print("This is an {} number".format(x))
    time.sleep(.5)
    print("Go ahead and guess now! ")
    

def pick():
    guesses = 0

    while guesses < 6:
        time.sleep(0.25)
        enter = input("Guess: ")

        try:
            guess = int(enter)
            if guess <= 100 and guess >=1:
                guesses = guesses + 1

                if guesses < 6:
                    if guess < number:
                        print("The guess of number that you have entered is too low")
                    if guess > number:
                        print("The guess of the number you entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")

                    if guess == number:
                        break

            if guess > 100 or guess < 1:
                print("This number is not in the range.")
                time.sleep(0.25)
                print("Please enter a number between 1 and 100")

        except:
            print("I don't think that "+enter+" is a number")
    if guess == number:
        guesses = str(guesses)
        print("Good job {}! You guessed my number in {} guesses!".format(name, guesses))
    if guess != number:
        print("Nope. The number I was thinking of was "+ str(number))

playagain = "Yes"

while playagain == "yes" or playagain == "y" or playagain == "Yes":
    intro()
    pick()
    print("Do you want to play again?")
    playagain = input()