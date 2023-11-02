def solution():
    """Iain has 200 pennies. He realizes that 30 of his pennies are older than he is. If he wishes to get rid of these pennies and then throw out 20% of his remaining pennies, how many will he have left?"""
    # Define the total number of pennies Iain has
    total_pennies = 200

    # Define the number of older pennies Iain has
    older_pennies = 30

    # Calculate the number of pennies Iain will have after getting rid of the older pennies
    new_total_pennies = total_pennies - older_pennies

    # Calculate the number of pennies Iain will throw out
    throw_out_pennies = int(new_total_pennies * 0.2)

    # Calculate the number of pennies Iain will have left
    left_pennies = new_total_pennies - throw_out_pennies

    # Display the number of pennies Iain will have left
    result = left_pennies
    return result

print(solution())