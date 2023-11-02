def solution():
    """The Period 1 gym class has 5 fewer than twice as many students as in the Period 2 gym class. There are 11 students in the Period 1 gym class. How many are in the Period 2 gym class?"""
    period1_students = 11
    period2_students = (period1_students + 5) / 2
    result = period2_students
    return result

print(solution())