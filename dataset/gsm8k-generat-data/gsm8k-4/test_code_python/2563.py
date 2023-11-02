def solution():
    """Sam has 18 cows. 5 more than half the cows are black. How many cows are not black?"""
    # Define the total number of cows
    total_cows = 18

    # Calculate half the cows and add 5 to get the number of black cows
    black_cows = (total_cows / 2) + 5

    # Calculate the number of cows that are not black
    not_black_cows = total_cows - black_cows

    # return the result
    result = not_black_cows
    return result

print(solution())