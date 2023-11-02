def solution():
     whole_pies = 4
     sold_pies = 1
     gifted_pies = 1
     pieces_per_pie = 6
     total_pieces = whole_pies * pieces_per_pie
     eaten_pieces = 2/3 * total_pieces
     remaining_pieces = total_pieces - sold_pies - gifted_pies - eaten_pieces
     result = remaining_pieces
     return result

print(solution())