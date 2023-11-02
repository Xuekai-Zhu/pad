def solution():
    total_students = 300  # Total number of students in the class
    smoking_students = int(total_students * 0.4)  # Number of smoking students in the class
    hospitalized_students = int(smoking_students * 0.7)  # Number of smoking students hospitalized from smoking-related complications
    non_hospitalized_students = smoking_students - hospitalized_students  # Number of smoking students who have not been hospitalized

    result = non_hospitalized_students
    return result

print(solution())