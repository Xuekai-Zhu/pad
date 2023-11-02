def solution():
    """Manny had 3 birthday cookie pies to share with his 24 classmates and his teacher, Mr. Keith. If each of the cookie pies were cut into 10 slices and Manny, his classmates, and Mr. Keith all had 1 piece, how many slices are left?"""
    total_slices = 3 * 10
    num_people = 24 + 1
    num_pieces = num_people * 1
    slices_left = total_slices - num_pieces
    result = slices_left
    return result

print(solution())