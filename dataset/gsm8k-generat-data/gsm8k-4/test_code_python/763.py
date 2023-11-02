def solution():
    """Josh has 18 yards of ribbon that is to be used equally to 6 gifts. If each gift will use 2 yards of ribbon, how many yards of ribbon will be left?"""
    # Define the total yards of ribbon and the number of gifts
    total_yards = 18
    num_gifts = 6

    # Calculate the total yards of ribbon needed for all the gifts
    total_gifts_yards = num_gifts * 2

    # Calculate the yards of ribbon left after making all the gifts
    yards_left = total_yards - total_gifts_yards

    # Return the result
    result = yards_left
    return result

print(solution())