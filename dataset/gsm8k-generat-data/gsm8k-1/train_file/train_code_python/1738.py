def solution():
    """The class plans to take a field trip to the zoo. The cost to rent a school bus is $100. The cost of admission is $10 per student. The teacher is allowed in for free. If the class has a budget of $350, how many students can go on the field trip?"""
    bus_cost = 100
    admission_cost = 10
    teacher_cost = 0
    total_budget = 350
    max_students = (total_budget - bus_cost - teacher_cost) // admission_cost
    result = max_students
    return result

print(solution())