def solution():
    # Calculate Eva's marks in the first semester
    maths_first = 80 + 10
    arts_first = 90 - 15
    science_first = (2/3) * 90

    # Calculate the total marks for each subject
    maths_total = maths_first + 80
    arts_total = arts_first + 90
    science_total = science_first + 90

    # Calculate the total marks for both semesters
    total_marks = maths_total + arts_total + science_total
    result = total_marks
    return result

print(solution())