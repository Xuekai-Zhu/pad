def solution():
    # Calculate the number of jellybeans guessed by the fourth student
    guess1 = 100
    guess2 = 8 * guess1
    guess3 = guess2 - 200
    average = (guess1 + guess2 + guess3) / 3
    guess4 = average + 25
    result = guess4
    return result

print(solution())