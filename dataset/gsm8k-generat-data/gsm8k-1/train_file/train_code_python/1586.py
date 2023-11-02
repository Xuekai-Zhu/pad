def solution():
    """In a class of 300 students, the number of smoking teens is 40% of the class. In a year, 70% of the smoking students are hospitalized from smoking-related complications. Calculate the total number of smoking students from the class who have not been hospitalized from smoking-related complications."""
    total_students = 300
    smoking_students = total_students * 0.4
    hospitalized_students = smoking_students * 0.7
    non_hospitalized_students = smoking_students - hospitalized_students
    result = non_hospitalized_students
    return result

print(solution())