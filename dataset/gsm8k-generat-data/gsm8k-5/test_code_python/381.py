def solution():
    monday_minutes = 450
    tuesday_minutes = monday_minutes / 2  # half the minutes worked on Monday
    wednesday_minutes = 300

    # Calculate the difference between Wednesday and Tuesday's work minutes
    difference_minutes = wednesday_minutes - tuesday_minutes
    result = difference_minutes
    return result

print(solution())