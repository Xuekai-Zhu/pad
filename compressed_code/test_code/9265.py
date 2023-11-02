def solution():
    
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