def solution():
    
    remaining_slices = 1
    pieces_of_toast = 10
    slices_per_piece_of_toast = 2
    total_slices = (pieces_of_toast * slices_per_piece_of_toast) + remaining_slices + 6
    result = total_slices
    return result

print(solution())