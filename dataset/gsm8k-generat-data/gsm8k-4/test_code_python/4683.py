def solution():
    """The Period 1 gym class has 5 fewer than twice as many students as in the Period 2 gym class. There are 11 students in the Period 1 gym class. How many are in the Period 2 gym class?"""
    
    # Define variables
    p1 = 11 # number of students in period 1
    p2 = None # number of students in period 2

    # Solve equation for p2
    p2 = (2*p1 - 5) / 2

    # Return result
    result = int(p2)
    return result

print(solution())