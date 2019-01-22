import random




def main():
    problem1()
    problem2()
    # problem3()
    problem4()

    # Python Program that creates a random number and prints that number


def problem1():
    randomNum = random.randint(0, 100)
    print(randomNum)

    # Python program that quits when the user tyoes quit


def problem2():
    while (True):
        userInput = input("Enter quit to exit")
        if (userInput == "quit"):
            break
        else:
            print("Unable to to Quit Program!")

    #Python program thats Creates a function that creates a random number. then Asks the user to guess the random number.
    # Keep letting the user guess until they get it right, then quit. If they don't get it right, tell them if their
    # next guess has to be higher or lower.


def problem4():
    randomNum = random.randint(0, 20)
    userInput = input("Guess the Number")
    if userInput == randomNum:
        print("Correct")
    elif userInput != randomNum:
        print("Keep Guessing")
    elif userInput < 10:
        print("HIGHER")
    elif userInput > 10:
        print("LOWER")


if __name__ == '__main__':
    main()
