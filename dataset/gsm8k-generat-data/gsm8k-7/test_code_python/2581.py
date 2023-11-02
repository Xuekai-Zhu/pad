def solution():
    money_kenneth_has = 50
    num_baguettes = 2
    baguette_cost = 2
    num_bottles_of_water = 2
    bottle_of_water_cost = 1

    # Calculate the total cost of all baguettes
    total_baguettes_cost = num_baguettes * baguette_cost

    # Calculate the total cost of all bottles of water
    total_bottles_of_water_cost = num_bottles_of_water * bottle_of_water_cost

    # Calculate the total cost of all items bought
    total_cost = total_baguettes_cost + total_bottles_of_water_cost

    # Calculate the amount of money Kenneth has left
    money_left = money_kenneth_has - total_cost
    result = money_left
    return result

print(solution())