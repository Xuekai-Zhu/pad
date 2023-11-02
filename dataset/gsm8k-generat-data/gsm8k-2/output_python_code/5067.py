def solution():
    """Emma bought a loaf of bread that had a certain number of slices. Her little cousin Andy ate 3 slices from the bread at two different points in time, and then Emma decided she would make toast with the remaining slices. If she uses 2 slices of bread to make 1 piece of toast bread, how many slices were in the original loaf if she was able to make 10 pieces of toast bread and had 1 slice of bread left?"""
    remaining_slices = 1
    pieces_of_toast = 10
    slices_per_piece_of_toast = 2
    total_slices = (pieces_of_toast * slices_per_piece_of_toast) + remaining_slices + 6
    result = total_slices
    return result

print(solution())