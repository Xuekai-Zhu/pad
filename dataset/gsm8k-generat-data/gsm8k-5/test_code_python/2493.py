def solution():
    eggs_per_cake = 2  # The recipe requires 2 eggs per cake
    milk_per_cake = 4  # The recipe requires 4 cups of milk per cake
    servings_per_cake = 4  # The recipe makes a cake for 4 people
    servings_needed = 8  # Tyler wants to make a cake for 8 people
    eggs_on_hand = 3  # Tyler has 3 eggs in the fridge

    # Calculate the total number of cakes Tyler needs to make for 8 people
    cakes_needed = servings_needed / servings_per_cake

    # Calculate the total number of eggs Tyler needs for the cakes
    eggs_needed = cakes_needed * eggs_per_cake

    # Calculate the number of eggs Tyler needs to buy
    eggs_to_buy = eggs_needed - eggs_on_hand
    result = eggs_to_buy
    return result

print(solution())