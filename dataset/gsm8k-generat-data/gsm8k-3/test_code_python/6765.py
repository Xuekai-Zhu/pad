def solution():
    """Hunter saw 5 frogs sitting on top lily pads in the pond. Three more frogs climbed out of the water onto logs floating in the pond. Then two dozen baby frogs hopped onto a big rock jutting out from the pond. How many frogs did Hunter see in the pond?"""
    # Initialize the number of frogs
    num_frogs = 5

    # Add the three frogs on the logs
    num_frogs += 3

    # Add the two dozen baby frogs
    num_frogs += 2*12

    # Display the total number of frogs
    result = num_frogs
    return result

print(solution())