def solution():
    """Danny has 3 bottles of soda. He drinks 90% of one bottle and gives 70% of the other two bottles to his friends. How much soda does Danny have left, expressed as a percentage of a bottle?"""
    # Define the initial amount of soda in one bottle
    initial_soda = 1

    # Calculate the amount of soda Danny has left after drinking from one bottle
    remaining_soda = (1 - 0.9) * initial_soda

    # Calculate the amount of soda given to friends
    given_soda = 2 * 0.7 * initial_soda

    # Calculate the total amount of soda Danny has left
    total_soda = remaining_soda + given_soda

    # Calculate the percentage of a bottle that Danny has left
    percentage_left = (total_soda / initial_soda) * 100

    # return the result
    result = percentage_left
    return result

print(solution())