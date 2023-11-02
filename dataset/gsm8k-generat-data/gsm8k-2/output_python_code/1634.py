def solution():
    """Janet's grades for her first semester of college were 90, 80, 70, and 100. If her semester 2 average was 82 percent, how much higher was her semester 1 average compared to her semester 2 average?"""
    semester1_grades = [90, 80, 70, 100]
    semester2_average = 82
    semester1_average = sum(semester1_grades) / len(semester1_grades)
    difference = semester1_average - semester2_average
    result = difference
    return result

print(solution())