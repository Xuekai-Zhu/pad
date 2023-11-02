def solution():
    # Calculate the current square footage of the smaller house
    current_small_house = 5200
    # Calculate the current square footage of the larger house
    current_large_house = 7300
    # Calculate the total current square footage
    total_current_square_footage = current_small_house + current_large_house
    # Calculate the square footage needed for the total to be 16,000
    needed_square_footage = 16000 - total_current_square_footage
    # Calculate the amount of expansion for the smaller house
    expansion_amount = needed_square_footage - (current_large_house - current_small_house)
    result = expansion_amount
    return result

print(solution())