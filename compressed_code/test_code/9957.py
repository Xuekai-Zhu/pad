def solution():
    
    total_pieces = 240
    eaten_percent = 60
    remaining_percent = 100 - eaten_percent
    remaining_pieces = total_pieces * (remaining_percent / 100)
    pieces_per_sister = remaining_pieces / 3
    result = pieces_per_sister
    return result

print(solution())