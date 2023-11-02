def solution():
    # Calculate the marks in first semester based on the given conditions
    maths_first = 80 + 10
    arts_first = 90 - 15
    science_second = 90 / (2/3)

    # Calculate the total marks in each subject for both semesters
    maths_total = maths_first + 80
    arts_total = arts_first + 90
    science_total = science_second + 90

    # Calculate the total marks for both semesters combined
    total_marks = maths_total + arts_total + science_total
    result = total_marks
    return result

print(solution())