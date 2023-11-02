def solution():
    """The class plans to take a field trip to the zoo. The cost to rent a school bus is $100. The cost of admission is $10 per student. The teacher is allowed in for free. If the class has a budget of $350, how many students can go on the field trip?"""
    # Define the cost of the school bus and admission per student
    BUS_COST = 100
    ADMISSION_COST = 10

    # Define the budget for the field trip
    budget = 350

    # Calculate the maximum number of students that can go on the field trip
    max_students = (budget - BUS_COST) // ADMISSION_COST

    # Display the maximum number of students
    result = max_students
    return result

print(solution())