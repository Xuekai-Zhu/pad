def solution():
    
    total_students = 300
    smoking_students = total_students * 0.4
    hospitalized_students = smoking_students * 0.7
    non_hospitalized_students = smoking_students - hospitalized_students
    result = non_hospitalized_students
    return result

print(solution())