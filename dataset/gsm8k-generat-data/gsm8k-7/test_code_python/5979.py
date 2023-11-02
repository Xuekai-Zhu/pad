def solution():
    sixth_grade_gpa = 93
    seventh_grade_gpa = sixth_grade_gpa + 2
    eighth_grade_gpa = 91

    # Calculate the total GPA for all three grades
    total_gpa = (sixth_grade_gpa + seventh_grade_gpa + eighth_grade_gpa)

    # Calculate the average GPA for the school
    average_gpa = total_gpa / 3
    result = average_gpa
    return result

print(solution())