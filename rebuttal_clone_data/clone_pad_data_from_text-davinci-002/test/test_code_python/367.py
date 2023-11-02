def solution():
    compartments = 12
    pennies_per_compartment = 2
    pennies_added = 6
    total_pennies = (compartments * pennies_per_compartment) + (compartments * pennies_added)
    result = total_pennies
    return result

print(solution())