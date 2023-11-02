def solution():
    num_students = 3
    num_red_pens_per_student = 62
    num_black_pens_per_student = 43
    total_pens_taken_first_month = 37
    total_pens_taken_second_month = 41

    # Calculate the initial number of pens bought
    num_initial_red_pens = num_students * num_red_pens_per_student
    num_initial_black_pens = num_students * num_black_pens_per_student

    # Calculate the total number of pens taken over the two months
    total_pens_taken = total_pens_taken_first_month + total_pens_taken_second_month

    # Calculate the total number of pens remaining
    num_remaining_pens = num_initial_red_pens + num_initial_black_pens - total_pens_taken

    # Calculate the number of pens each student will get
    pens_per_student = num_remaining_pens / num_students
    result = pens_per_student
    return result

print(solution())