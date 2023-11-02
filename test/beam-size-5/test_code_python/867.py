def solution():
    
    total_pieces = 60
    day1_pieces = total_pieces * (2/5)
    day2_pieces = 10
    remaining_pieces = total_pieces - day1_pieces - day2_pieces
    day3_pieces = remaining_pieces * (7/13)
    total_pieces_eaten = day1_pieces + day2_pieces + day3_pieces
    result = total_pieces_eaten
    return result

print(solution())