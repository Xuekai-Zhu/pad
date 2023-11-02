def solution():
    # Calculate the number of eggs and cups of milk needed to make an eight-person cake
    eggs_needed = 2 * 2  # double the number of eggs for a four-person cake
    milk_needed = 4 * 2  # double the cups of milk for a four-person cake

    # Calculate the number of eggs Tyler needs to buy
    eggs_to_buy = eggs_needed - 3  # Tyler has 3 eggs in the fridge already
    result = eggs_to_buy
    return result

print(solution())