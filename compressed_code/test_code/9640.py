def solution():
    
    total_pens = 342
    num_students = 44
    pens_per_student = 7
    pens_given_out = num_students * pens_per_student
    pens_left = total_pens - pens_given_out
    pens_in_locker = pens_left // 2
    pens_taken_home = pens_left - pens_in_locker
    result = pens_taken_home
    return result

print(solution())