def solution():
    """Jan is making candy necklaces for herself and a few friends. Everyone receives a candy necklace each and each candy necklace is made up of 10 pieces of candies. The pieces of candies come from blocks of candy, which each produce 30 pieces of candy. If Jan breaks down 3 blocks of candy and every single piece of candy from this is used in the candy necklaces, how many friends receive a candy necklace?"""
    # Define the number of candies produced by one block of candy
    CANDIES_PER_BLOCK = 30

    # Calculate the total number of candies obtained from the 3 blocks of candy
    total_candies = 3 * CANDIES_PER_BLOCK

    # Calculate the number of friends who can receive a candy necklace
    num_friends = total_candies // 10

    # Display the number of friends who can receive a candy necklace
    result = num_friends
    return result

print(solution())