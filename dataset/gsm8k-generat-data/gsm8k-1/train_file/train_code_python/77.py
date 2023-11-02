def solution():
    """Manny had 3 birthday cookie pies to share with his 24 classmates and his teacher, Mr. Keith. If each of the cookie pies were cut into 10 slices and Manny, his classmates, and Mr. Keith all had 1 piece, how many slices are left?"""
    num_pies = 3
    num_people = 24 + 1  # classmates + teacher
    slices_per_pie = 10
    total_slices = num_pies * slices_per_pie
    slices_taken = num_people * 1
    slices_left = total_slices - slices_taken
    result = slices_left
    return result

print(solution())