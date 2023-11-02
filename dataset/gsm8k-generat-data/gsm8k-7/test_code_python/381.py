def solution():
    monday_minutes = 450
    tuesday_minutes = monday_minutes / 2  # half of what he worked on Monday
    wednesday_minutes = 300

    # Calculate the difference between Wednesday and Tuesday
    difference = wednesday_minutes - tuesday_minutes
    result = difference
    return result

print(solution())