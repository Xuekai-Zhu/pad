def solution():
    # Define the number of pens Sally started with
    start_pens = 342

    # Define the number of students in Sally's class
    num_students = 44

    # Define the number of pens Sally gave to each student
    pens_per_student = 7

    # Calculate the total pens given to students
    total_pens_given = num_students * pens_per_student

    # Calculate the remaining pens after giving to students
    remaining_pens = start_pens - total_pens_given

    # Calculate the number of pens Sally left in her locker
    left_in_locker = remaining_pens / 2

    # Calculate the number of pens Sally took home
    pens_taken_home = remaining_pens - left_in_locker

    result = pens_taken_home
    return result

print(solution())