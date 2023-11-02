def solution():
    gallon_cost = 8
    ounce_cost = 3
    ounce_per_gallon = 128  # 1 gallon = 128 ounces

    # Calculate the cost of buying the same amount of mayo at the normal store
    normal_store_cost = (ounce_per_gallon / 16) * ounce_cost

    # Calculate the amount saved by buying the gallon container
    savings = normal_store_cost - gallon_cost
    result = savings
    return result

print(solution())