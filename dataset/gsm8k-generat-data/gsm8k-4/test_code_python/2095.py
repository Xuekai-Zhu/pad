def solution():
    """There are 60 pieces of chips in Lara's bag. One-sixth of the chips are blue. There are 34 red chips and the rest are green. How many green chips are in Lara's bag?"""
    # Define the total number of chips and the number of blue chips
    total_chips = 60
    blue_chips = total_chips // 6

    # Calculate the number of red chips
    red_chips = 34

    # Calculate the number of green chips
    green_chips = total_chips - blue_chips - red_chips

    # return the result
    result = green_chips
    return result

print(solution())