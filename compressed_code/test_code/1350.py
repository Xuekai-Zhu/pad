def solution():
    
    bus_cost = 100
    admission_cost = 10
    teacher_cost = 0
    total_budget = 350
    remaining_budget = total_budget - bus_cost - teacher_cost
    max_students = remaining_budget // admission_cost
    result = max_students
    return result

print(solution())