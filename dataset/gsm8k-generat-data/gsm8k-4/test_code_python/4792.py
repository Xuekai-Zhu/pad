def solution():
    """Nancy creates 12 clay pots on Monday, twice as many on Tuesday, a few more on Wednesday, then ends the week with 50 clay pots. How many did she create on Wednesday?"""
    # Calculate the number of pots on Tuesday
    tuesday_pots = 12 * 2

    # Calculate the remaining number of pots
    remaining_pots = 50 - 12 - tuesday_pots

    # The number of pots created on Wednesday is the remaining number of pots
    wednesday_pots = remaining_pots

    result = wednesday_pots
    return result

print(solution())