def solution():
    """Hunter saw 5 frogs sitting on top lily pads in the pond. Three more frogs climbed out of the water onto logs floating in the pond. Then two dozen baby frogs hopped onto a big rock jutting out from the pond.  How many frogs did Hunter see in the pond?"""
    # Define the number of frogs initially seen on the lily pads
    initial_frogs = 5

    # Define the number of frogs that climbed onto the logs
    log_frogs = 3

    # Define the number of baby frogs on the rock
    baby_frogs = 24

    # Calculate the total number of frogs seen in the pond
    total_frogs = initial_frogs + log_frogs + baby_frogs

    result = total_frogs
    return result

print(solution())