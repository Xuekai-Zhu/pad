def solution():
    # Calculate the total number of candies from the 3 blocks
    total_candies = 3 * 30  # each block produces 30 pieces of candy

    # Calculate the number of friends who receive a candy necklace
    num_friends = total_candies // 10  # each necklace is made up of 10 pieces of candy

    result = num_friends
    return result

print(solution())