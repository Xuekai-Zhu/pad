def solution():
    """The average GPA for 6th graders is 93, the 7th graders is 2 more than the 6th graders and the 8th graders average GPA is 91. What is the average GPA for the school?"""
    sixth_grade_gpa = 93
    seventh_grade_gpa = sixth_grade_gpa + 2
    eighth_grade_gpa = 91
    total_gpa = sixth_grade_gpa + seventh_grade_gpa + eighth_grade_gpa
    average_gpa = total_gpa / 3
    result = average_gpa
    return result

print(solution())