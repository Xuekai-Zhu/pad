def solution():
    # Set the cost and size of each item
    candy_cost = 1
    candy_size = 12
    chip_cost = 1.4
    chip_size = 17

    # Calculate the cost per ounce of each item
    candy_cost_per_ounce = candy_cost / candy_size
    chip_cost_per_ounce = chip_cost / chip_size

    # Determine which item is cheaper per ounce and calculate the number of ounces that can be bought with $7
    if candy_cost_per_ounce < chip_cost_per_ounce:
        item = "candy"
        size = candy_size
        number_of_items = 7 // candy_cost
    else:
        item = "chips"
        size = chip_size
        number_of_items = 7 // chip_cost

    # Calculate the total number of ounces of the chosen item
    total_ounces = number_of_items * size

    # Set the result
    result = total_ounces

    return result

print(solution())