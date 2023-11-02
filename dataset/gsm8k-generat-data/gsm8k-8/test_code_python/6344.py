def solution():
    # Calculate the total amount of juice in liters
    total_juice_liters = 5 * 2

    # Convert the glass capacity from milliliters to liters
    glass_capacity_liters = 0.25

    # Calculate the maximum number of glasses that can be filled
    max_num_glasses = total_juice_liters / glass_capacity_liters

    # Round down to get the integer number of glasses that can be filled
    num_full_glasses = int(max_num_glasses)

    result = num_full_glasses
    return result

print(solution())