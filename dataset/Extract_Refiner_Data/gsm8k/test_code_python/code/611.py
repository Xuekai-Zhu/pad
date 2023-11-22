def solution():
    
    # Define the prices of rocks and coral
    rock_price = 2.5
    coral_price = 2

    # Define the prices of fish and food
    fish_price = 0.5
    fish_food_price = 2

    # Calculate the total cost of the rocks
    rock_cost = 2 * rock_price

    # Calculate the total cost of the coral
    coral_cost = 3 * coral_price

    # Calculate the total cost of the fish
    fish_cost = 20 * fish_price

    # Calculate the total cost of the fish food
    fish_food_cost = 20 * fish_food_price

    # Calculate the total cost of all the items
    total_cost = rock_cost + coral_cost + fish_cost + fish_food_cost

    # return the result
    result = total_cost
    return result

print(solution())