def solution():
    shampoo_per_wash = 0.25  # in ounces
    shampoo_bottle_size = 14  # in ounces
    num_days = 366  # leap year

    # Calculate the total amount of shampoo Brittany will use over the year
    total_shampoo_used = shampoo_per_wash * (num_days // 2)

    # Calculate the number of shampoo bottles needed
    num_bottles = total_shampoo_used / shampoo_bottle_size

    # Round up to the nearest whole number of bottles
    num_bottles = math.ceil(num_bottles)

    result = num_bottles
    return result

print(solution())