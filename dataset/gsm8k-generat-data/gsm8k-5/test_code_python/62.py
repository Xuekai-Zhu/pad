def solution():
    total_liters = 290  # There are 290 liters of oil in 24 cans
    known_liters = 10 * 8  # 10 cans hold 8 liters each

    # Calculate the total liters in the remaining cans
    remaining_liters = total_liters - known_liters

    # Calculate the number of cans that hold the remaining liters
    remaining_cans = 24 - 10

    # Calculate the liters per can for the remaining cans
    liters_per_can = remaining_liters / remaining_cans
    result = liters_per_can
    return result

print(solution())