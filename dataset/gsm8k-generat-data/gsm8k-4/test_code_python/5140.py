def solution():
    """There were 28 students inside a bus before stopping at an intersection.
    After stopping at an intersection, there were 58 students on the bus.
    What's 40% of the number of students who entered the bus at the intermediate stop?"""
    # Calculate the number of students who entered the bus at the intermediate stop
    intermediate_students = 58 - 28

    # Calculate 40% of the number of intermediate students
    forty_percent = intermediate_students * 0.4

    result = forty_percent
    return result

print(solution())