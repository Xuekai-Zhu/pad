def solution():
    
    green_pieces = 35
    green_percent = 25
    total_percent = 100
    total_pieces = (green_pieces * total_percent) / green_percent
    clear_pieces = total_pieces - (green_pieces + 20)
    result = clear_pieces
    return result

print(solution())