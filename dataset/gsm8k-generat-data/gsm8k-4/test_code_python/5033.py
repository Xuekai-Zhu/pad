def solution():
    """Ray always takes the same route when he walks his dog. First, he walks 4 blocks to the park. Then he walks 7 blocks to the high school. Finally, he walks 11 blocks to get back home. Ray walks his dog 3 times each day. How many blocks does Ray's dog walk each day?"""
    # Define the number of blocks Ray walks for each trip
    blocks_per_trip = 4 + 7 + 11

    # Calculate the number of blocks Ray's dog walks each day
    total_blocks = blocks_per_trip * 3

    result = total_blocks
    return result

print(solution())