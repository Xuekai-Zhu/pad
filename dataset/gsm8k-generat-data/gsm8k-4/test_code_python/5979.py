def solution():
    """The average GPA for 6th graders is 93, the 7th graders is 2 more than the 6th graders and the 8th graders average GPA is 91. What is the average GPA for the school?"""
    # Define the average GPA for each grade
    sixth_grade_GPA = 93
    seventh_grade_GPA = sixth_grade_GPA + 2
    eighth_grade_GPA = 91

    # Calculate the total GPA by adding the GPA for each grade and dividing by the number of grades
    total_GPA = sixth_grade_GPA + seventh_grade_GPA + eighth_grade_GPA
    num_grades = 3
    school_GPA = total_GPA / num_grades

    result = school_GPA
    return result

print(solution())