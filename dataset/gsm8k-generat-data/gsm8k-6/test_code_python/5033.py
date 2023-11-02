def solution():
    # Calculate the total number of blocks Ray walks in one trip
    total_blocks = 4 + 7 + 11  

    # Calculate the total number of blocks Ray's dog walks in one trip
    dog_blocks = total_blocks * 2  # Ray's dog is walking with him, so they cover the same distance

    # Calculate the total number of blocks Ray's dog walks in one day
    daily_blocks = dog_blocks * 3  # Ray walks his dog 3 times a day

    result = daily_blocks
    return result

print(solution())