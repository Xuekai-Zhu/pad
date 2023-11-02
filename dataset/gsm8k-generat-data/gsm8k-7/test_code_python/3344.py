def solution():
    num_pennies = 123
    num_nickels = 85
    num_dimes = 35
    total_change = 0.48  # in dollars
    cost_per_scoop = 3.0
    num_family_members = 5

    # Calculate the total amount of change in the jar
    total_jar_change = (num_pennies * 0.01) + (num_nickels * 0.05) + (num_dimes * 0.10)

    # Calculate the total cost of all the ice cream scoops for the family
    total_ice_cream_cost = cost_per_scoop * num_family_members

    # Calculate the amount of change that the family should have after buying the ice cream
    expected_change = total_jar_change - total_ice_cream_cost

    # Calculate the number of quarters in the jar
    num_quarters = int((expected_change - total_change) / 0.25)
    result = num_quarters
    return result

print(solution())