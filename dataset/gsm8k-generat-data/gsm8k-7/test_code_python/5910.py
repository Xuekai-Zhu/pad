def solution():
    num_cups = 5
    cup_size_before = 8  # in ounces
    shrink_ratio = 0.5
    
    # Calculate the total amount of coffee before shrinking
    total_coffee_before = num_cups * cup_size_before

    # Calculate the total amount of coffee after shrinking
    total_coffee_after = total_coffee_before * shrink_ratio

    result = total_coffee_after
    return result

print(solution())