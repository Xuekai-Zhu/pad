def solution():
    # Calculate the total marks scored by Eva in all the semesters
    math_marks = 80 + (80 + 10)  # Eva scored ten more marks in maths in the first semester than the second
    arts_marks = 90 + (90 - 15)  # Eva scored 15 marks less in arts in the first semester than the second
    science_marks = 90 + (90 * 2 / 3)  # Eva scored 1/3 marks less in science in the first semester than the second
    total_marks = math_marks + arts_marks + science_marks  # total marks scored by Eva in all the semesters
    result = total_marks
    return result

print(solution())