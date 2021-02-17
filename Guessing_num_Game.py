import Guess_the_num_function #importing Guess_the_num_function for Guess function.


while True:
    try:
        #Asking to user for inputs start and end numbers. try exception block helps us 
        start = int(input("Give a starting number of the range..."))
        end = int(input("Give a ending number of the range..."))
        #codition for starting number must be lessthan ending number in range
        #and input number must be number
        if start < end:
            Guess_the_num_function.Guess(start,end)
            break
        else:
            print("Starting number is must be lessthen ending number...\nEnding number is must be greater than starting number...")
    except ValueError:
        print("Input value must be number...")