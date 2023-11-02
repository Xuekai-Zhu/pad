def solution():
     total_pens = 342
     pens_per_student = 7
     remaining_pens = total_pens % (pens_per_student * 44)
     pens_left_in_locker = remaining_pens / 2
     pens_taken_home = remaining_pens - pens_left_in_locker
     result = pens_taken_home
     return result

print(solution())