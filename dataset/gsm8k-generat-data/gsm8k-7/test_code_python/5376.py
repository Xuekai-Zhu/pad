def solution():
    # Marks in second semester
    maths_marks_sec2 = 80
    arts_marks_sec2 = 90
    science_marks_sec2 = 90

    # Calculate marks in first semester using the given differences
    maths_marks_sec1 = maths_marks_sec2 + 10
    arts_marks_sec1 = arts_marks_sec2 - 15
    science_marks_sec1 = (2/3) * science_marks_sec2

    # Calculate total marks
    total_marks = maths_marks_sec1 + maths_marks_sec2 + arts_marks_sec1 + arts_marks_sec2 + science_marks_sec1 + science_marks_sec2
    result = total_marks
    return result

print(solution())