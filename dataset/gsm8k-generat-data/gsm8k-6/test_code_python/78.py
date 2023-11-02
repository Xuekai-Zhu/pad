def solution():
    # Calculate the total number of people to share the cookie pies
    total_people = 24 + 1  # 24 classmates and 1 teacher

    # Calculate the total number of slices needed
    total_slices = 3 * 10 * (total_people) # 3 cookie pies, each with 10 slices, for total_people

    # Calculate the number of slices left
    slices_left = total_slices - (total_people * 1)  # each person had 1 slice

    result = slices_left
    return result

print(solution())