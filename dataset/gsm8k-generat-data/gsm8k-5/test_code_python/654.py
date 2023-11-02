def solution():
    pennies_per_compartment = 2  # There are 2 pennies in each compartment initially
    compartments = 12  # There are 12 compartments in the piggy bank

    # Calculate the total number of pennies in the piggy bank initially
    initial_total = pennies_per_compartment * compartments

    # Calculate the total number of pennies after adding 6 to each compartment
    new_pennies_per_compartment = pennies_per_compartment + 6
    new_total = new_pennies_per_compartment * compartments

    # Calculate the total number of pennies Roshesmina has
    total_pennies = initial_total + new_total
    result = total_pennies
    return result

print(solution())