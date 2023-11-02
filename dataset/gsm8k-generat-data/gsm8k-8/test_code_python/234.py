def solution():
    # Calculate the total cost of the bread and cheese
    total_cost = 4.20 + 2.05

    # Calculate the amount of change Mark should receive
    change = 7.00 - total_cost

    # Calculate the number of quarters and dimes needed for the change
    num_quarters = 1
    num_dimes = 1
    remaining_change = change - 0.35

    # Calculate the number of nickels needed for the remaining change
    num_nickels = int(remaining_change / 0.05)

    result = num_nickels
    return result

print(solution())