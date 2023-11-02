def solution():
    """Jan is making candy necklaces for herself and a few friends. Everyone receives a candy necklace each and each candy necklace is made up of 10 pieces of candies. The pieces of candies come from blocks of candy, which each produce 30 pieces of candy. If Jan breaks down 3 blocks of candy and every single piece of candy from this is used in the candy necklaces, how many friends receive a candy necklace?"""
    # Define the total number of pieces of candy
    total_candy_pieces = 3 * 30

    # Calculate the number of friends who can receive a candy necklace
    num_friends = total_candy_pieces // 10

    # return the result
    result = num_friends
    return result

print(solution())