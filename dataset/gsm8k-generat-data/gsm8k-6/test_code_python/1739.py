def solution():
    class_budget = 350  # budget for the field trip
    bus_rental_cost = 100  # cost to rent a school bus
    admission_cost_per_student = 10  # cost of admission per student
    teacher_count = 1  # teacher is allowed in for free

    # Calculate the maximum number of students that can go on the field trip within the given budget
    max_students = (class_budget - bus_rental_cost) // admission_cost_per_student - teacher_count
    result = max_students
    return result

print(solution())