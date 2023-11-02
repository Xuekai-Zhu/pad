def solution():
    # Calculate the total number of pens each student received initially
    initial_pens = 62 + 43
    total_pens = 3 * initial_pens

    # Calculate the total number of pens taken from the pool
    total_taken = 37 + 41

    # Calculate the remaining pens
    remaining_pens = total_pens - total_taken

    # Calculate the number of pens each student will receive now
    each_student = remaining_pens // 3
    result = each_student
    return result

print(solution())