def solution():
    """Sally took 342 pens to her class of 44 students. If she gave 7 pens to each student, left half of the remainder in her locker, and took the rest home, how many did she take home?"""
    total_pens = 342
    total_students = 44
    pens_per_student = 7
    pens_given_out = total_students * pens_per_student
    pens_leftover = total_pens - pens_given_out
    pens_in_locker = pens_leftover // 2
    pens_taken_home = pens_leftover - pens_in_locker
    result = pens_taken_home
    return result

print(solution())