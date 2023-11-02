def solution():
    # Define the initial number of pennies in one compartment
    initial_pennies = 2

    # Define the number of compartments
    num_compartments = 12

    # Add 6 pennies to each compartment
    new_pennies = initial_pennies + 6

    # Calculate the total number of pennies
    total_pennies = new_pennies * num_compartments
    result = total_pennies
    return result

print(solution())