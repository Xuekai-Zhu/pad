def solution():
    pieces_per_block = 30  # Each block of candy produces 30 pieces of candy
    pieces_per_necklace = 10  # Each candy necklace has 10 pieces of candy
    blocks_used = 3  # Jan breaks down 3 blocks of candy

    # Calculate the total number of pieces of candy Jan has
    total_pieces = pieces_per_block * blocks_used

    # Calculate the total number of candy necklaces Jan can make
    total_necklaces = total_pieces // pieces_per_necklace  # we use floor division to get the whole number of necklaces

    # Jan makes a necklace for herself and a few friends, so the number of friends who receive a necklace is the total number of necklaces minus 1
    num_friends = total_necklaces - 1
    result = num_friends
    return result

print(solution())