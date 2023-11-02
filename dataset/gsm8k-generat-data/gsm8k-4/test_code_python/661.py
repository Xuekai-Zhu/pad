def solution():
    """There are 30 different nuts in a bowl. If 5/6 of the nuts were eaten, how many nuts were left?"""
    # Define the initial number of nuts and the fraction that was eaten
    initial_nuts = 30
    fraction_eaten = 5/6

    # Calculate the number of nuts that were eaten
    nuts_eaten = initial_nuts * fraction_eaten

    # Calculate the number of nuts that were left
    nuts_left = initial_nuts - nuts_eaten

    # return the result
    result = nuts_left
    return result

print(solution())