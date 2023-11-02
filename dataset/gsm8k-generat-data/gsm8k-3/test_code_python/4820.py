def solution():
    """Danny has 3 bottles of soda. He drinks 90% of one bottle and gives 70% of the other two bottles to his friends. How much soda does Danny have left, expressed as a percentage of a bottle?"""
    # Define the initial amount of soda
    initial_amount = 3

    # Calculate the amount of soda Danny drinks
    drank_amount = 0.9

    # Calculate the amount of soda Danny gives to his friends
    given_amount = 0.7 * 2

    # Calculate the remaining amount of soda
    remaining_amount = initial_amount - drank_amount - given_amount

    # Express the remaining amount as a percentage of a bottle
    remaining_percentage = remaining_amount / initial_amount * 100

    # Display the remaining amount as a percentage of a bottle
    result = remaining_percentage
    return result

print(solution())