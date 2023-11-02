def solution():
    # Calculate the total number of students present in both kindergarten sessions
    morning_present = 25 - 3  # 25 students registered for morning session but 3 were absent
    afternoon_present = 24 - 4  # 24 students registered for afternoon session but 4 were absent
    total_students = morning_present + afternoon_present
    result = total_students
    return result

print(solution())