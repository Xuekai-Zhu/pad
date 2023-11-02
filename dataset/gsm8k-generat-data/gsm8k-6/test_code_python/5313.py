def solution():
    # Calculate the number of cake pieces eaten by Forest and his friends
    eaten_pieces = 0.6 * 240

    # Calculate the number of pieces of cake left for Juelz and his sisters
    remaining_pieces = 240 - eaten_pieces

    # Calculate the number of pieces of cake each sister received
    pieces_per_sister = remaining_pieces / 3

    result = pieces_per_sister
    return result

print(solution())