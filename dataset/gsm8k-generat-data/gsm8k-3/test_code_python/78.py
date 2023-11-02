def solution():
    """Manny had 3 birthday cookie pies to share with his 24 classmates and his teacher, Mr. Keith. If each of the cookie pies were cut into 10 slices and Manny, his classmates, and Mr. Keith all had 1 piece, how many slices are left?"""
    # Define the number of cookie pies and the number of slices per pie
    cookie_pies = 3
    slices_per_pie = 10

    # Calculate the total number of slices
    total_slices = cookie_pies * slices_per_pie

    # Calculate the number of people who will have a slice
    num_people = 24 + 1

    # Calculate the number of slices eaten
    slices_eaten = num_people * 1

    # Calculate the number of slices left
    slices_left = total_slices - slices_eaten

    result = slices_left
    return result

print(solution())