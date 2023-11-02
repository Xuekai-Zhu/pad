def solution():
    """Eva learns for two semesters in a year. In 2019, she scored ten more marks in maths in the first semester than the second, 15 marks less in arts, and 1/3 marks less in science in the first semester than the second. If she got 80 marks in maths in the second semester, 90 marks in arts, and 90 in science, what's the total number of her marks in all the semesters?"""
    # Calculate the number of marks in maths in the first semester
    maths_2 = 80 # marks in maths in second semester
    maths_1 = maths_2 + 10

    # Calculate the number of marks in arts in the first semester
    arts_2 = 90 # marks in arts in second semester
    arts_1 = arts_2 - 15

    # Calculate the number of marks in science in the first semester
    science_2 = 90 # marks in science in second semester
    science_1 = science_2 * (2/3)

    # Calculate the total number of marks in both semesters
    total_marks = maths_1 + maths_2 + arts_1 + arts_2 + science_1 + science_2

    # Display the total number of marks
    result = total_marks
    return result

print(solution())