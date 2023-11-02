def solution():
    """The class has to guess how many jellybeans are in a jar the teacher brought in. He lets 4 students make their guesses. The first thinks it contains 100 jellybeans. The second says there are 8 times as many. The third guesses 200 less than the third. The fourth takes the average of the first three guesses, and then adds 25 to it. How many jellybeans did the fourth student guess? """
    # Define the guesses of the first three students
    guess1 = 100
    guess2 = guess1 * 8
    guess3 = guess2 - 200

    # Calculate the average of the first three guesses
    average = (guess1 + guess2 + guess3) / 3

    # Calculate the fourth guess
    guess4 = average + 25

    result = guess4
    return result

print(solution())