def solution():
    # Calculate the number of students who entered the bus at the intermediate stop
    students_entered = 58 - 28  # Number of students on the bus after the stop - number of students before the stop

    # Calculate 40% of the number of students who entered
    percentage = 0.4
    result = percentage * students_entered
    return result

print(solution())