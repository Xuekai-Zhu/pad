def solution():
    # Total number of boys and girls in 4th grade
    fourth_grade_girls = 12 + 15
    fourth_grade_boys = 13 + 11
    fourth_grade_total = fourth_grade_girls + fourth_grade_boys

    # Total number of boys and girls in 5th grade
    fifth_grade_girls = 9 + 10
    fifth_grade_boys = 13 + 11
    fifth_grade_total = fifth_grade_girls + fifth_grade_boys

    # Total number of boys and girls in both grades
    total_girls = fourth_grade_girls + fifth_grade_girls
    total_boys = fourth_grade_boys + fifth_grade_boys

    # Difference between total number of boys and girls
    difference = abs(total_boys - total_girls)
    result = difference
    return result

print(solution())