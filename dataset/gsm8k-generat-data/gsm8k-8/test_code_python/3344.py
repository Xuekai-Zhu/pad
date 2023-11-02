def solution():
    # Define the value of a double scoop
    double_scoop = 3

    # Calculate the total value of the change in the jar
    total_value = 123 * 0.01 + 85 * 0.05 + 35 * 0.1
    
    # Calculate the remaining value after buying ice cream
    remaining_value = total_value - 5 * double_scoop - 0.48

    # Calculate the number of quarters based on the remaining value
    quarters = int(remaining_value / 0.25)

    result = quarters
    return result

print(solution())