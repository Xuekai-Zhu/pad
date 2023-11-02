def solution():
    # Calculate the number of smoking students in the class
    smoking_students = 0.4 * 300  

    # Calculate the number of smoking students hospitalized
    hospitalized_students = 0.7 * smoking_students  

    # Calculate the number of smoking students not hospitalized
    not_hospitalized_students = smoking_students - hospitalized_students 
    result = not_hospitalized_students
    return result

print(solution())