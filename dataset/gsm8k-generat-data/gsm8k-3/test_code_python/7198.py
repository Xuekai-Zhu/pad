def solution():
    """After Betty gave Stuart 40% of her marble collection, the number of marbles in Stuart's collection increased to 80. If Betty had 60 marbles, how many marbles did Stuart have initially?"""
    # Define Betty's initial collection size
    betty_initial = 60

    # Calculate the size of the collection Stuart received
    stuart_received = 80 - betty_initial * 0.6

    # Calculate Stuart's initial collection size
    stuart_initial = stuart_received / 0.4

    # Display Stuart's initial collection size
    result = stuart_initial
    return result

print(solution())