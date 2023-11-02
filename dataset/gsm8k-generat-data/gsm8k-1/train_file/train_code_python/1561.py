def solution():
    """Jan is making candy necklaces for herself and a few friends. Everyone receives a candy necklace each and each candy necklace is made up of 10 pieces of candies. The pieces of candies come from blocks of candy, which each produce 30 pieces of candy. If Jan breaks down 3 blocks of candy and every single piece of candy from this is used in the candy necklaces, how many friends receive a candy necklace?"""
    pieces_per_block = 30
    pieces_per_necklace = 10
    total_pieces = pieces_per_block * 3
    necklaces = total_pieces // pieces_per_necklace
    friends = necklaces - 1 # Jan is making candy necklaces for herself and a few friends. "Everyone receives a candy necklace each", so this means Jan is included as one of the friends.
    result = friends
    return result

print(solution())