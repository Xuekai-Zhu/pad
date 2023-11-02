def solution():
    cookie_pie_slices = 3 * 10  # There are 3 cookie pies, each cut into 10 slices
    total_people = 24 + 1  # Manny's classmates and Mr. Keith make 25 people in total
    total_slices_used = total_people  # Each person had 1 slice

    # Calculate the number of slices left
    slices_left = cookie_pie_slices - total_slices_used
    result = slices_left
    return result

print(solution())