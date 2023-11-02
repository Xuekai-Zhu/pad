def solution():
    # Define the initial amounts
    marco = 24
    mary = 15

    # Calculate how much Marco gives Mary
    marco_gives = marco / 2

    # Calculate the new amounts after the giving and spending
    marco -= marco_gives
    mary += marco_gives
    mary -= 5

    # Calculate how much more money Mary has than Marco
    difference = mary - marco
    result = difference
    return result

print(solution())