def solution():
    """John buys a box of 40 light bulbs. He uses 16 of them and then gives half of what is left to a friend. How many does he have left?"""
    # Define the initial number of light bulbs
    total_bulbs = 40

    # Subtract the number of bulbs used by John
    bulbs_left = total_bulbs - 16

    # Calculate the number of bulbs given to John's friend
    bulbs_given = bulbs_left / 2

    # Calculate the number of bulbs left with John
    bulbs_left = bulbs_left - bulbs_given

    # return the result
    result = int(bulbs_left)
    return result

print(solution())