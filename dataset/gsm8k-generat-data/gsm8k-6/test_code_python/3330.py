def solution():
    # Calculate the total number of pens that Jane bought
    total_red_pens = 62 * 3
    total_black_pens = 43 * 3
    total_pens = total_red_pens + total_black_pens

    # Calculate the total number of pens they took from the pool
    total_pens_taken = 37 + 41

    # Calculate the number of pens they have left
    remaining_pens = total_pens - total_pens_taken

    # Calculate the number of pens each student will get
    pens_per_student = remaining_pens / 3
    result = pens_per_student
    return result

print(solution())