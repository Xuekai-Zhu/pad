def solution():
    # Calculate the total number of sections in the bus
    total_sections = 13 * 2  # 13 rows with 2 sections in each row
    # Calculate the total number of students that can be seated in the bus
    total_students = total_sections * 2  # 2 students can sit in each section
    result = total_students
    return result

print(solution())