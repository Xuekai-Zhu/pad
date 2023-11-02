def solution():
    blocks_to_park = 4
    blocks_to_high_school = 7
    blocks_back_home = 11
    walks_per_day = 3

    # Calculate the total number of blocks Ray walks in one trip
    total_blocks_walked = blocks_to_park + blocks_to_high_school + blocks_back_home

    # Calculate the total number of blocks Ray's dog walks in one trip
    dog_blocks_walked = total_blocks_walked

    # Calculate the total number of blocks Ray's dog walks in one day
    total_dog_blocks_walked = dog_blocks_walked * walks_per_day
    result = total_dog_blocks_walked
    return result

print(solution())