def solution():
    """If there are two pennies in each of the twelve compartments of Roshesmina's piggy bank and she adds 6 more pennies to each compartment, calculate the total number of pennies she has?"""
    # Define the initial number of pennies in each compartment
    initial_pennies = 2

    # Define the number of compartments
    compartments = 12

    # Define the number of pennies added to each compartment
    added_pennies = 6

    # Calculate the new number of pennies in each compartment
    new_pennies = initial_pennies + added_pennies

    # Calculate the total number of pennies
    total_pennies = new_pennies * compartments

    # return the result
    result = total_pennies
    return result

print(solution())