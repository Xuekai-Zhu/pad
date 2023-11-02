def solution():
    # Calculate the number of lollipops for the first 45 students
    lollipops_first = 45 // 5

    # Calculate the number of lollipops for the additional 15 students
    lollipops_second = 15 // 5

    # Calculate the total number of lollipops
    total_lollipops = lollipops_first + lollipops_second
    result = total_lollipops
    return result

print(solution())