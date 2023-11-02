def solution():
    # Calculate the total number of hours both Cathy and Chris were supposed to work
    total_hours = 20 * 4 * 2

    # Calculate the number of hours Chris missed due to being sick
    chris_sick_hours = 20 * 1

    # Calculate the total number of hours worked by both Cathy and Chris
    total_worked_hours = total_hours - chris_sick_hours

    # Calculate the number of hours worked by Cathy
    cathy_hours = total_worked_hours / 2

    result = cathy_hours
    return result

print(solution())