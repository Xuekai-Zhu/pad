def solution():
    """Grace baked 4 whole pumpkin pies. She sold 1 whole pumpkin pie and gave 1 whole pumpkin pie to her friend. 
    The remaining whole pumpkin pies were each sliced into 6 pieces. Her family ate 2/3 pieces. 
    How many pieces of pumpkin pie were left?"""
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