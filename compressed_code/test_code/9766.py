def solution():
    
    slices_left = 1
    pieces_of_toast = 10
    slices_per_piece_of_toast = 2
    slices_eaten = 6
    total_slices = (pieces_of_toast * slices_per_piece_of_toast) + slices_left + slices_eaten
    result = total_slices
    return result

print(solution())