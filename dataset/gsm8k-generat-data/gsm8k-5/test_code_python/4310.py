def solution():
    yesterday_students = 70  # Yesterday there were 70 students in the science class
    absent_today = 30  # Today, there are 30 students absent
    present_today = (2 * yesterday_students) * 0.9  # Ten percent less than twice the total students present yesterday

    # Calculate the total number of students registered for the course
    total_students = present_today + absent_today
    result = total_students
    return result

print(solution())