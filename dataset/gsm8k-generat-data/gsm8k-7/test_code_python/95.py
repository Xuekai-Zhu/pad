def solution():
    num_quarters = 20
    num_nickels = num_quarters * 5   # Convert quarters to nickels
    iron_nickels_percent = 0.20
    iron_nickels_value = 3

    # Calculate the number of iron nickels
    num_iron_nickels = int(num_nickels * iron_nickels_percent)

    # Calculate the value of non-iron nickels
    non_iron_nickels_value = (num_nickels - num_iron_nickels) * 0.05

    # Calculate the total value of all nickels, including iron ones
    total_nickels_value = (num_iron_nickels * iron_nickels_value) + non_iron_nickels_value

    # Add the value of the quarters
    total_value = (num_quarters * 0.25) + total_nickels_value
    result = total_value
    return result

print(solution())