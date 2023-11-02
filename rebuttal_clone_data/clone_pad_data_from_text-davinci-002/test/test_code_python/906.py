def solution():
    class_size = 300
    smoking_students = class_size * 0.4
    non_smoking_students = class_size - smoking_students
    hospitalization_rate = 0.7
    hospitalized_students = smoking_students * hospitalization_rate
    non_hospitalized_students = smoking_students - hospitalized_students
    result = non_hospitalized_students
    
    return result

print(solution())