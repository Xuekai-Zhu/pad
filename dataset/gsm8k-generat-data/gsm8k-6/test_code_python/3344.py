def solution():
    # Calculate the total value of the change in the jar
    total_value = 123 * 0.01 + 85 * 0.05 + 35 * 0.1 + x * 0.25  # x is the number of quarters

    # Calculate the total cost of the ice cream
    ice_cream_cost = 3 * 5

    # Calculate the remaining change after the ice cream trip
    remaining_change = total_value - ice_cream_cost - 0.48

    # Calculate the number of quarters in the jar
    num_quarters = int(remaining_change / 0.25)
    result = num_quarters
    return result

print(solution())