def solution():
    
    total_pies = 4
    sold_pies = 1
    given_pies = 1
    remaining_pies = total_pies - sold_pies - given_pies
    pieces_per_pie = 6
    total_pieces = remaining_pies * pieces_per_pie
    eaten_pieces = (2/3) * total_pieces
    remaining_pieces = total_pieces - eaten_pieces
    result = remaining_pieces
    return result

print(solution())