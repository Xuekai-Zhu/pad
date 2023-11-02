def solution():
    """In a class of 300 students, the number of smoking teens is 40% of the class. In a year, 70% of the smoking students are hospitalized from smoking-related complications. Calculate the total number of smoking students from the class who have not been hospitalized from smoking-related complications."""
    class_size = 300
    smoking_percentage = 0.4
    smoking_students = class_size * smoking_percentage
    hospitalized_percentage = 0.7
    hospitalized_students = smoking_students * hospitalized_percentage
    non_hospitalized_students = smoking_students - hospitalized_students
    result = non_hospitalized_students
    return result

print(solution())