def solution():
    """Of the 600 students at River Falls High School, 3/4 of them play tennis. Of those that play tennis, 60% of them also play hockey. How many students play both hockey and tennis?"""
    # Define the total number of students and the fraction that play tennis
    total_students = 600
    tennis_fraction = 3/4

    # Calculate the number of students that play tennis
    tennis_students = total_students * tennis_fraction

    # Calculate the number of students that play both hockey and tennis
    hockey_tennis_students = tennis_students * 0.6

    # Return the result
    result = hockey_tennis_students
    return result

print(solution())