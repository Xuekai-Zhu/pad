def solution():
    """Ray always takes the same route when he walks his dog. First, he walks 4 blocks to the park. Then he walks 7 blocks to the high school. Finally, he walks 11 blocks to get back home. Ray walks his dog 3 times each day. How many blocks does Ray's dog walk each day?"""
    # Define the number of blocks Ray walks for each trip
    trip_blocks = 4 + 7 + 11

    # Calculate the total number of blocks Ray's dog walks each day
    total_blocks = trip_blocks * 3

    # Display the total blocks
    result = total_blocks
    return result

print(solution())