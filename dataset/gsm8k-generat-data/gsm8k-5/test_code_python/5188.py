def solution():
    total_students = 325  # Total number of students in the high school
    glasses_percent = 40  # Percentage of students who have glasses
    glasses_students = (glasses_percent / 100) * total_students  # Calculate the number of students who have glasses
    no_glasses_students = total_students - glasses_students  # Calculate the number of students who do not have glasses
    result = no_glasses_students
    return result

print(solution())