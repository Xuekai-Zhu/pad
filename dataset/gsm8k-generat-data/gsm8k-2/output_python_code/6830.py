def solution():
    """The class has to guess how many jellybeans are in a jar the teacher brought in. He lets 4 students make their guesses. The first thinks it contains 100 jellybeans. The second says there are 8 times as many. The third guesses 200 less than the third. The fourth takes the average of the first three guesses, and then adds 25 to it. How many jellybeans did the fourth student guess?"""
    first_guess = 100
    second_guess = 8 * first_guess
    third_guess = second_guess - 200
    fourth_guess = (first_guess + second_guess + third_guess) / 3 + 25
    result = fourth_guess
    return result

print(solution())