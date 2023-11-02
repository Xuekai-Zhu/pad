def solution():
    morning_reg = 25
    morning_absent = 3
    afternoon_reg = 24
    afternoon_absent = 4

    # Calculate the number of students present for each session
    morning_present = morning_reg - morning_absent
    afternoon_present = afternoon_reg - afternoon_absent

    # Calculate the total number of students over both sessions
    total_students = morning_present + afternoon_present
    result = total_students
    return result

print(solution())