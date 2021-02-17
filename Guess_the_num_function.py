import random

def Guess(x,y):
    random_number = random.randint(x,y)
    # Guess variable is 0 bcz we are making it integer
    count = 0
    Guess = 0
    while Guess != random_number:
        try:
            Guess = int(input("Guess a number between {} to {}...".format(x,y)))
            if Guess > y or Guess < x:
                print("Your guess is outoff range...")
            elif Guess < random_number:
                print("sry, guess again. Your number is too low...")
            elif Guess > random_number:
                print("sry, guess again. Your numher is too high...")
        except ValueError:
            print("Input value must be number...")
        count = count + 1
    print("Yay! Your guess is correct, that is {}".format(Guess))
    print("Guess count {}".format(count))


#your guess is in no.of times(count)
