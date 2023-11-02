def solution():
    """Evergreen Elementary school has 100 students in Grades 4, 5, and 6. There are 30 students in Grade 4 and 35 students in Grade 5. How many students are in Grade 6?"""
    # Define the number of students in Grade 4 and 5
    grade_4 = 30
    grade_5 = 35

    # Calculate the number of students in Grade 6
    grade_6 = 100 - grade_4 - grade_5

    # Display the number of students in Grade 6
    result = grade_6
    return result

print(solution())