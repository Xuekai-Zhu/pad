def solution():
    """Janet's grades for her first semester of college were 90, 80, 70, and 100. If her semester 2 average was 82 percent, how much higher was her semester 1 average compared to her semester 2 average?"""
    # Define the grades for the first semester
    semester1_grades = [90, 80, 70, 100]

    # Calculate the average grade for the first semester
    semester1_average = sum(semester1_grades) / len(semester1_grades)

    # Define the average grade for the second semester
    semester2_average = 82

    # Calculate the difference between the two averages
    average_difference = semester1_average - semester2_average

    # return the result
    result = average_difference
    return result

print(solution())