def solution():
    # Calculate the number of students present for the morning session
    morning_present = 25 - 3

    # Calculate the number of students present for the afternoon session
    afternoon_present = 24 - 4

    # Calculate the total number of students present
    total_present = morning_present + afternoon_present

    result = total_present
    return result

print(solution())