def solution():
    # Calculate the number of pennies in each compartment after adding 6 more pennies
    new_pennies = 2 + 6  # Roshesmina adds 6 more pennies to each compartment
    pennies_per_compartment = new_pennies * 2  # there are two pennies in each compartment

    # Calculate the total number of pennies
    total_pennies = pennies_per_compartment * 12
    result = total_pennies
    return result

print(solution())