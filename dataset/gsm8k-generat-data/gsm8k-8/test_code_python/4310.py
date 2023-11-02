def solution():
    # Calculate the total number of students present yesterday
    total_yesterday = 70

    # Calculate the number of students present today
    present_today = 0.9 * (2 * total_yesterday - 30)

    # Calculate the total number of students registered for the course
    total_registered = present_today + 30
    result = total_registered
    return result

print(solution())