def solution():
    """Wilson decides to go sledding on some nearby hills. On the 2 tall hills, he sleds down them 4 times each and on the 3 small hills, he sled down them half as often as he sleds down the tall hills. How many times did he sled down the hills?"""
    # Define the number of times Wilson sleds down each tall hill
    TALL_HILL_SLEDS = 4

    # Define the number of small hills
    SMALL_HILLS = 3

    # Wilson sleds down each small hill half as often as he sleds down each tall hill
    SMALL_HILL_SLEDS = TALL_HILL_SLEDS / 2

    # Calculate the total number of times Wilson sleds down the hills
    total_sleds = (TALL_HILL_SLEDS * 2) + (SMALL_HILL_SLEDS * 3)

    # Display the total number of times Wilson sleds down the hills
    result = total_sleds
    return result

print(solution())