def solution():
    total_nuts = 30
    fraction_eaten = 5/6

    # Calculate the number of nuts that were eaten
    num_eaten = total_nuts * fraction_eaten

    # Calculate the number of nuts left
    nuts_left = total_nuts - num_eaten
    result = nuts_left
    return result

print(solution())