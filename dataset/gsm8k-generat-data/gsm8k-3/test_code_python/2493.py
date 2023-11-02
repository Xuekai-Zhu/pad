def solution():
    """The recipe for a four-person cake requires 2 eggs and 4 cups of milk. Tyler wants to use this recipe to make a cake for eight people. If Tyler has 3 eggs in the fridge, how many more eggs does Tyler need to buy?"""
    # Define the number of eggs and cups of milk required for a 4-person cake
    EGGS_PER_CAKE = 2
    MILK_PER_CAKE = 4

    # Calculate the number of eggs and cups of milk required for an 8-person cake
    eggs_needed = EGGS_PER_CAKE * 2
    milk_needed = MILK_PER_CAKE * 2

    # Determine how many more eggs Tyler needs to buy
    eggs_to_buy = eggs_needed - 3  # Tyler has 3 eggs in the fridge

    # Display the number of eggs Tyler needs to buy
    result = eggs_to_buy
    return result

print(solution())