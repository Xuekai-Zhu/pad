def solution():
     bus_rental_cost = 100
     student_admission_cost = 10
     budget = 350
     teacher_admission_cost = 0
     number_of_students = (budget - bus_rental_cost) / student_admission_cost
     result = number_of_students
     return result

print(solution())