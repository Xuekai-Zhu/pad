def solution():
    """A jar contains 9 blue pens, 21 black pens, and 6 red pens. Four blue pens are removed and then seven black pens are removed. How many pens are left in the jar? """
    # Define the number of pens in the jar
    blue_pens = 9
    black_pens = 21
    red_pens = 6

    # Remove 4 blue pens
    blue_pens -= 4

    # Remove 7 black pens
    black_pens -= 7

    # Calculate the total number of pens left in the jar
    total_pens = blue_pens + black_pens + red_pens

    # Display the total number of pens left in the jar
    result = total_pens
    return result

print(solution())