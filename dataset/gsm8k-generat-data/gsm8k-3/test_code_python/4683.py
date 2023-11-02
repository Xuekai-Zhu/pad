def solution():
    """The Period 1 gym class has 5 fewer than twice as many students as in the Period 2 gym class. There are 11 students in the Period 1 gym class. How many are in the Period 2 gym class?"""
    # Define the number of students in Period 1 and the relationship between the number of students in Period 1 and Period 2
    period_1_students = 11
    period_2_students = (period_1_students + 5) / 2

    # Display the number of students in Period 2
    result = period_2_students
    return result

print(solution())