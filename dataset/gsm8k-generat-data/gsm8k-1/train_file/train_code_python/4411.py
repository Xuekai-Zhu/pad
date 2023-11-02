def solution():
    """Mrs. Young buys a 300 piece puzzle set for her three sons. She divides the pieces evenly to the three boys. Reyn can place 25 pieces into the puzzle picture. Rhys places twice as much as Reyn. Rory places three times as much as Reyn. Altogether, how many puzzle pieces are still left to be placed?"""
    total_pieces = 300
    num_of_boys = 3
    pieces_per_boy = total_pieces / num_of_boys
    reyn_pieces = 25
    rhys_pieces = reyn_pieces * 2
    rory_pieces = reyn_pieces * 3
    total_placed = reyn_pieces + rhys_pieces + rory_pieces
    pieces_left = total_pieces - total_placed
    result = pieces_left
    return result

print(solution())