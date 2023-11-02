def solution():
     
     total_students = 80
     percent_in_A = 40
     num_in_A = total_students * (percent_in_A / 100)
     num_in_B = num_in_A - 21
     num_in_C = total_students - num_in_A - num_in_B
     result = num_in_C
     return result

print(solution())