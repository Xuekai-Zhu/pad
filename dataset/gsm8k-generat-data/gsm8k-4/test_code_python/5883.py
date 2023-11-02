def solution():
    """Iain has 200 pennies. He realizes that 30 of his pennies are older than he is. If he wishes to get rid of these pennies and then throw out 20% of his remaining pennies, how many will he have left?"""
    # Define the initial number of pennies
    initial_pennies = 200

    # Calculate the number of pennies to get rid of
    to_get_rid_of = 30

    # Calculate the number of remaining pennies
    remaining_pennies = initial_pennies - to_get_rid_of

    # Calculate the number of pennies to throw out
    to_throw_out = remaining_pennies * 0.2

    # Calculate the final number of pennies
    final_pennies = int(remaining_pennies - to_throw_out)

    # Display the final number of pennies
    result = final_pennies
    return result

print(solution())