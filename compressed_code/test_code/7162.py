def solution():
    
    bus_cost = 100
    admission_cost = 10
    teacher_cost = 0
    total_budget = 350
    max_students = (total_budget - bus_cost - teacher_cost) // admission_cost
    result = max_students
    return result

print(solution())