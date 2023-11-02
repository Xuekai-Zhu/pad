def solution():
    guess1 = 100
    guess2 = 8 * guess1
    guess3 = guess2 - 200
    guess4 = (guess1 + guess2 + guess3)/3 + 25
    result = guess4
    return result

print(solution())