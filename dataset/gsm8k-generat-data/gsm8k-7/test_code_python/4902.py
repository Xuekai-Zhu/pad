def solution():
    num_pens = 342
    num_students = 44
    pens_per_student = 7

    # Calculate the total number of pens given to the students
    total_given = num_students * pens_per_student

    # Calculate the remainder pens
    remainder = num_pens - total_given

    # Calculate the pens left in her locker
    left_in_locker = remainder // 2

    # Calculate the pens taken home
    taken_home = remainder - left_in_locker
    result = taken_home
    return result

print(solution())