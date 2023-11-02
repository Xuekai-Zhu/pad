def solution():
    
    green_pieces = 35
    green_percent = 0.25
    total_pieces = (green_pieces / green_percent)
    amber_pieces = 20
    clear_pieces = total_pieces - green_pieces - amber_pieces
    result = clear_pieces
    return result

print(solution())