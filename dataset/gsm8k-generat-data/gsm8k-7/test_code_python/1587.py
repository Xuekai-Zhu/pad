def solution():
    total_students = 300
    smoking_percentage = 0.4
    hospitalized_percentage = 0.7

    # Calculate the number of smoking students
    smoking_students = total_students * smoking_percentage

    # Calculate the number of smoking students who have been hospitalized
    hospitalized_students = smoking_students * hospitalized_percentage

    # Calculate the number of smoking students who have not been hospitalized
    non_hospitalized_students = smoking_students - hospitalized_students
    result = non_hospitalized_students
    return result

print(solution())