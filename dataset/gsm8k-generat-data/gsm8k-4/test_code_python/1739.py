def solution():
    """The class plans to take a field trip to the zoo. The cost to rent a school bus is $100. The cost of admission is $10 per student. The teacher is allowed in for free. If the class has a budget of $350, how many students can go on the field trip?"""
    # Define the cost of renting a school bus and the cost of admission per student
    BUS_RENTAL_COST = 100
    ADMISSION_COST_PER_STUDENT = 10

    # Define the available budget and the number of students that can go on the field trip
    available_budget = 350
    num_students = 0

    # Calculate the maximum number of students that can go on the field trip based on the available budget
    while (num_students * ADMISSION_COST_PER_STUDENT) + BUS_RENTAL_COST <= available_budget:
        num_students += 1

    result = num_students
    return result

print(solution())