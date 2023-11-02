def solution():
    percentage_in_band = 0.2  # 20% of the students are in the band
    students_in_band = 168  # There are 168 students in the band

    # Calculate the total number of students in the middle school
    total_students = students_in_band / percentage_in_band
    result = total_students
    return result

print(solution())