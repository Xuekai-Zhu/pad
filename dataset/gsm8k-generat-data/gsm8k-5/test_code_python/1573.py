def solution():
    # Calculate the hours worked on Monday and Tuesday
    monday_hours = 4
    tuesday_hours = monday_hours - 2

    # Calculate the hours worked on Wednesday
    wednesday_hours = 2 * monday_hours

    # Calculate the hours worked on Thursday
    thursday_hours = 2 * tuesday_hours

    # Calculate the total hours worked
    total_hours = monday_hours + tuesday_hours + wednesday_hours + thursday_hours
    result = total_hours
    return result

print(solution())