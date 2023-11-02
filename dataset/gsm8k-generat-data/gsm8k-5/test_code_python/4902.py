def solution():
    total_pens = 342  # Sally took 342 pens to her class
    num_students = 44  # There are 44 students in her class
    pens_per_student = 7  # Sally gave 7 pens to each student

    # Calculate the total number of pens given to the students
    pens_given_out = num_students * pens_per_student

    # Calculate the remainder of pens
    remaining_pens = total_pens - pens_given_out

    # Calculate the number of pens left in Sally's locker
    pens_in_locker = remaining_pens // 2

    # Calculate the number of pens Sally took home
    pens_taken_home = remaining_pens - pens_in_locker
    result = pens_taken_home
    return result

print(solution())