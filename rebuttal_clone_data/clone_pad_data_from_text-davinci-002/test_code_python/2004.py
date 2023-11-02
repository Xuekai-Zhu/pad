def solution():
     total_marks = 400
     first_test = 80
     second_test = first_test + 10
     third_test = (total_marks - (first_test + second_test)) / 2
     result = third_test
     return result

print(solution())