def solution():
    # Define the number of whole pumpkin pies
    whole_pies = 4

    # Calculate how many whole pumpkin pies are left after selling and giving away
    left_whole_pies = whole_pies - 2

    # Calculate how many total pieces of pumpkin pie are left
    total_pieces = left_whole_pies * 6

    # Calculate how many pieces of pumpkin pie Grace's family ate
    family_pieces = (2/3) * total_pieces

    # Calculate how many pieces of pumpkin pie are left
    left_pieces = total_pieces - family_pieces
    result = left_pieces
    return result

print(solution())