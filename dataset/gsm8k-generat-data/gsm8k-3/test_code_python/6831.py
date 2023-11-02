def solution():
    """The class has to guess how many jellybeans are in a jar the teacher brought in. He lets 4 students make their guesses. The first thinks it contains 100 jellybeans. The second says there are 8 times as many. The third guesses 200 less than the third. The fourth takes the average of the first three guesses, and then adds 25 to it. How many jellybeans did the fourth student guess?"""
    # Define the first three guesses
    guess_1 = 100
    guess_2 = 8 * guess_1
    guess_3 = guess_2 - 200

    # Calculate the average of the first three guesses
    average = (guess_1 + guess_2 + guess_3) / 3

    # Calculate the fourth guess
    guess_4 = average + 25

    # Display the fourth guess
    result = guess_4
    return result

print(solution())