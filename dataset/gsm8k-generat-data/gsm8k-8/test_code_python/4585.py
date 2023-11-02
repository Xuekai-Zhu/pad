def solution():
    # Convert 2 liters to milliliters
    ml_in_liter = 1000
    total_milk = 2 * ml_in_liter

    # Divide the total milk by the size of one portion
    portion_size = 200
    portions = total_milk // portion_size
    result = portions
    return result

print(solution())