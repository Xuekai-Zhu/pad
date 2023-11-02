def solution():
    """There are 30 different nuts in a bowl. If 5/6 of the nuts were eaten, how many nuts were left?"""
    # Define the number of nuts in the bowl
    total_nuts = 30

    # Calculate the number of nuts that were eaten
    eaten_nuts = total_nuts * (5/6)

    # Calculate the number of nuts that were left
    left_nuts = total_nuts - eaten_nuts

    # Display the number of nuts that were left
    result = left_nuts
    return result

print(solution())