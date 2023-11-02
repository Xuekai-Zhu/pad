def solution():
     boys = 15
     girls = boys * 1.2
     new_girls = 2 * girls
     new_students = new_girls - girls
     total_students = boys + girls + new_students
     result = total_students
     return result

print(solution())