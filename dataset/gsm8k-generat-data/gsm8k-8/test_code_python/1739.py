def solution():
    # Define the costs and budget
    bus_cost = 100
    admission_cost_per_student = 10
    teacher_cost = 0
    total_budget = 350

    # Calculate the maximum number of students who can go on the trip
    max_students = (total_budget - bus_cost - teacher_cost) / admission_cost_per_student
    result = max_students
    return result

print(solution())