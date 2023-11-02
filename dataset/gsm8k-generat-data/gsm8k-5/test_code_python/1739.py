def solution():
    bus_rental_cost = 100  # Cost to rent a school bus is $100
    admission_cost_per_student = 10  # Cost of admission is $10 per student
    teacher_admission_cost = 0  # Teacher gets in for free
    total_budget = 350  # Total budget for the field trip is $350

    # Calculate the maximum number of students that can go on the field trip
    max_students = (total_budget - bus_rental_cost - teacher_admission_cost) / admission_cost_per_student
    result = max_students
    return result

print(solution())