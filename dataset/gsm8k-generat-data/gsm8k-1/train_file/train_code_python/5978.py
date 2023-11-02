def solution():
    """The average GPA for 6th graders is 93, the 7th graders is 2 more than the 6th graders and the 8th graders average GPA is 91. What is the average GPA for the school?"""
    sixth_grade_avg = 93
    seventh_grade_avg = sixth_grade_avg + 2
    eighth_grade_avg = 91
    total_grades = 3
    school_avg = (sixth_grade_avg + seventh_grade_avg + eighth_grade_avg) / total_grades
    result = school_avg
    return result

print(solution())