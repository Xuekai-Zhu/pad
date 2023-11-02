def solution():
    """Lisa is making a pizza. She uses 30 pieces of pepperoni for a pizza, twice as many pieces of ham, and 12 more pieces of sausage than pepperoni. If there are 6 slices of pizza, and everything was distributed evenly, how many pieces of meat altogether are on each slice?"""
    pepperoni_pieces = 30
    ham_pieces = 2 * pepperoni_pieces
    sausage_pieces = pepperoni_pieces + 12
    total_meat_pieces = pepperoni_pieces + ham_pieces + sausage_pieces
    pieces_per_slice = total_meat_pieces / 6
    result = pieces_per_slice
    return result

print(solution())