def solution():
    """Jan is making candy necklaces for herself and a few friends. Everyone receives a candy necklace each and each candy necklace is made up of 10 pieces of candies. The pieces of candies come from blocks of candy, which each produce 30 pieces of candy. If Jan breaks down 3 blocks of candy and every single piece of candy from this is used in the candy necklaces, how many friends receive a candy necklace?"""
    blocks_of_candy = 3
    pieces_per_block = 30
    total_pieces = blocks_of_candy * pieces_per_block
    necklaces_per_person = 1
    pieces_per_necklace = 10
    total_necklaces = total_pieces // pieces_per_necklace
    num_friends = total_necklaces // necklaces_per_person
    result = num_friends
    return result

print(solution())