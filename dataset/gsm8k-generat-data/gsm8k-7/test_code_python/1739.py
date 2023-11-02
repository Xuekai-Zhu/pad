def solution():
    bus_rental_cost = 100
    admission_cost_per_student = 10
    teacher_admission_cost = 0
    total_budget = 350

    # Calculate the maximum number of students that can go on the field trip based on the total budget
    max_num_students = (total_budget - bus_rental_cost - teacher_admission_cost) / admission_cost_per_student
    result = max_num_students
    return result

print(solution())