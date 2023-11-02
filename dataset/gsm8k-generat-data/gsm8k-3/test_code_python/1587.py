def solution():
    """In a class of 300 students, the number of smoking teens is 40% of the class. In a year, 70% of the smoking students are hospitalized from smoking-related complications. Calculate the total number of smoking students from the class who have not been hospitalized from smoking-related complications."""
    # Define the total number of students and the percentage of smoking students
    total_students = 300
    smoking_percentage = 0.4

    # Calculate the number of smoking students
    smoking_students = total_students * smoking_percentage

    # Calculate the number of smoking students who have been hospitalized
    hospitalized_smokers = smoking_students * 0.7

    # Calculate the number of smoking students who have not been hospitalized
    non_hospitalized_smokers = smoking_students - hospitalized_smokers

    # Display the number of smoking students who have not been hospitalized
    result = non_hospitalized_smokers
    return result

print(solution())