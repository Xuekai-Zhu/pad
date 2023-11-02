def solution():
    """The recipe for a four-person cake requires 2 eggs and 4 cups of milk. Tyler wants to use this recipe to make a cake for eight people. If Tyler has 3 eggs in the fridge, how many more eggs does Tyler need to buy?"""
    # Define the number of people for the cake and the number of eggs and cups of milk needed for four people
    people = 8
    eggs_4 = 2

    # Calculate the number of eggs needed for the desired number of people
    eggs_needed = (eggs_4 / 4) * people

    # Calculate the number of additional eggs needed
    eggs_to_buy = eggs_needed - 3

    result = eggs_to_buy
    return result

print(solution())