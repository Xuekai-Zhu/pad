def solution():
    """Grace baked 4 whole pumpkin pies. She sold 1 whole pumpkin pie and gave 1 whole pumpkin pie to her friend. The remaining whole pumpkin pies were each sliced into 6 pieces. Her family ate 2/3 pieces. How many pieces of pumpkin pie were left?"""
    whole_pies = 4
    pies_sold = 1
    pies_given_away = 1
    pies_left = whole_pies - pies_sold - pies_given_away
    pieces_per_pie = 6
    total_pieces = pies_left * pieces_per_pie
    pieces_eaten = (2/3) * total_pieces
    pieces_left = total_pieces - pieces_eaten
    result = pieces_left
    return result

print(solution())