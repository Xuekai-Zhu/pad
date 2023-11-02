def solution():
    """Manny had 3 birthday cookie pies to share with his 24 classmates and his teacher, Mr. Keith. If each of the cookie pies were cut into 10 slices and Manny, his classmates, and Mr. Keith all had 1 piece, how many slices are left?"""
    # Define the number of cookie pies and the number of slices per pie
    cookie_pies = 3
    slices_per_pie = 10

    # Define the number of people who will eat the cookie pies
    total_people = 24 + 1

    # Calculate the total number of slices eaten
    total_slices = total_people * 1

    # Calculate the number of slices remaining
    slices_remaining = (cookie_pies * slices_per_pie) - total_slices

    # return the result
    result = slices_remaining
    return result

print(solution())