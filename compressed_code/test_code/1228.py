def solution():
    
    class_size = 300
    smoking_percentage = 0.4
    smoking_students = class_size * smoking_percentage
    hospitalized_percentage = 0.7
    hospitalized_students = smoking_students * hospitalized_percentage
    non_hospitalized_students = smoking_students - hospitalized_students
    result = non_hospitalized_students
    return result

print(solution())