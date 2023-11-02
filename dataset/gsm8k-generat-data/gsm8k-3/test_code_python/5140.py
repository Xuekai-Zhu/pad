def solution():
    """There were 28 students inside a bus before stopping at an intersection. 
    After stopping at an intersection, there were 58 students on the bus. 
    What's 40% of the number of students who entered the bus at the intermediate stop?"""
    # Calculate the number of students who entered the bus at the intermediate stop
    students_entered = 58 - 28

    # Calculate 40% of the students who entered the bus at the intermediate stop
    forty_percent = 0.4 * students_entered

    # Return the result
    result = forty_percent
    return result

print(solution())