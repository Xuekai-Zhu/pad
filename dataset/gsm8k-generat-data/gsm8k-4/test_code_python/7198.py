def solution():
    """After Betty gave Stuart 40% of her marble collection, the number of marbles in Stuart's collection increased to 80. If Betty had 60 marbles, how many marbles did Stuart have initially?"""
    # Define the initial number of marbles
    initial_marbles = None

    betty_marbles = 60
    stuart_marbles_after = 80
    percentage_given = 0.4

    # Calculate the number of marbles given to Stuart
    marbles_given = betty_marbles * percentage_given

    # Calculate the total number of marbles after the transfer
    total_marbles = stuart_marbles_after - marbles_given

    # Set the result to the initial number of marbles
    initial_marbles = total_marbles

    # Return the result
    result = initial_marbles
    return result

print(solution())