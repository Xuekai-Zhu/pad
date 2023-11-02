def solution():
    """Lisa is making a pizza. She uses 30 pieces of pepperoni for a pizza, twice as many pieces of ham, and 12 more pieces of sausage than pepperoni. If there are 6 slices of pizza, and everything was distributed evenly, how many pieces of meat altogether are on each slice?"""
    pepperoni = 30
    ham = pepperoni * 2
    sausage = pepperoni + 12
    total_meat = pepperoni + ham + sausage
    slices = 6
    pieces_per_slice = total_meat / slices
    result = pieces_per_slice
    return result

print(solution())