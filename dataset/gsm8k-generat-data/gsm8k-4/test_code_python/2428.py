def solution():
    """Wilson decides to go sledding on some nearby hills. On the 2 tall hills, he sleds down them 4 times each and on the 3 small hills, he sled down them half as often as he sleds down the tall hills. How many times did he sled down the hills?"""
    # Define the number of times Wilson sleds down the tall hills
    tall_hills_sleds = 4 * 2

    # Define the number of times Wilson sleds down each small hill
    small_hills_sleds = tall_hills_sleds / 2

    # Define the total number of times Wilson sleds down the hills
    total_sleds = tall_hills_sleds + small_hills_sleds * 3

    # return the result
    result = total_sleds
    return result

print(solution())