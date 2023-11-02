def solution():
    # Define the first three guesses
    guess1 = 100
    guess2 = 8 * guess1
    guess3 = guess2 - 200

    # Calculate the average of the first three guesses
    average_guess = (guess1 + guess2 + guess3) / 3

    # Calculate the fourth guess
    guess4 = average_guess + 25
    result = guess4
    return result

print(solution())