def solution():
    """Sally took 342 pens to her class of 44 students. If she gave 7 pens to each student, left half of the remainder in her locker, and took the rest home, how many did she take home?"""
    # Define the total number of pens Sally took to class
    total_pens = 342

    # Define the number of students in Sally's class
    num_students = 44

    # Calculate the number of pens Sally gave to each student
    pens_per_student = 7

    # Calculate the total number of pens Sally gave to students
    given_pens = num_students * pens_per_student

    # Calculate the number of pens Sally had left after giving each student 7 pens
    remaining_pens = total_pens - given_pens

    # Calculate the number of pens Sally left in her locker
    locker_pens = remaining_pens // 2

    # Calculate the number of pens Sally took home
    taken_home = remaining_pens - locker_pens

    # Return the result
    result = taken_home
    return result

print(solution())