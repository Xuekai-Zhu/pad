def solution():
    red_pens_per_student = 62
    black_pens_per_student = 43
    total_students = 3

    # Calculate the total number of pens each student has
    total_red_pens = red_pens_per_student * total_students
    total_black_pens = black_pens_per_student * total_students
    total_pens = total_red_pens + total_black_pens

    # Calculate the number of pens taken from the pool
    pens_taken = 37 + 41

    # Calculate the number of remaining pens
    remaining_pens = total_pens - pens_taken

    # Calculate the number of pens each student will get now
    pens_per_student = remaining_pens / total_students

    result = pens_per_student
    return result

print(solution())