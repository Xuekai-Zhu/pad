def solution():
    # Define the number of pieces of candy in a block
    candy_per_block = 30

    # Calculate the total number of pieces of candy from the 3 blocks
    total_candy = 3 * candy_per_block

    # Calculate the number of friends who receive a candy necklace
    num_friends = total_candy // 10

    result = num_friends
    return result

print(solution())