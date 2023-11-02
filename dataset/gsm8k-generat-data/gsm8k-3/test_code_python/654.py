def solution():
    """If there are two pennies in each of the twelve compartments of Roshesmina's piggy bank and she adds 6 more pennies to each compartment, calculate the total number of pennies she has?"""
    # Define the number of compartments and the initial number of pennies in each compartment
    compartments = 12
    initial_pennies = 2

    # Calculate the total number of pennies in the piggy bank after adding 6 more pennies to each compartment
    total_pennies = compartments * (initial_pennies + 6)

    # Display the total number of pennies
    result = total_pennies
    return result

print(solution())