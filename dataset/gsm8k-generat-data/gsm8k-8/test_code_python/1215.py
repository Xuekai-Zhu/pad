def solution():
    # Calculate the total number of servings needed
    total_servings = 2 * 6

    # Calculate the total volume of milk needed in ml
    total_milk_volume = total_servings * 250 * 0.5

    # Convert the total volume to liters
    total_milk_liters = total_milk_volume / 1000

    # Round up to the nearest whole number of cartons
    num_cartons = math.ceil(total_milk_liters)

    result = num_cartons
    return result

print(solution())