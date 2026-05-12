import random

secret_number = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Correct! You win.")
else:
    print("Wrong! The number was:", secret_number)

    # Explanation
    #
    # random.randint(1, 10)
    # generates
    # a
    # random
    # number.
    #
    # If
    # the
    # guess
    # equals
    # the
    # secret
    # number → user
    # wins.
    #
    # What
    # You
    # Learned in Stage
    # 2
    #
    # You
    # now
    # understand:
    #
    # if
    # else
    #     elif
    #     comparison
    #     operators
    #     for loops
    #         while loops
    #
    #     These
    #     are
    #     the
    #     decision and repetition
    #     tools
    #     of
    #     Python.