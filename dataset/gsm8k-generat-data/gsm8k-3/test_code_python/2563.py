def solution():
    """Sam has 18 cows. 5 more than half the cows are black. How many cows are not black?"""
    # Define the number of cows Sam has
    total_cows = 18

    # Calculate the number of black cows
    black_cows = (total_cows // 2) + 5

    # Calculate the number of cows that are not black
    not_black_cows = total_cows - black_cows

    # Display the number of cows that are not black
    result = not_black_cows
    return result

print(solution())