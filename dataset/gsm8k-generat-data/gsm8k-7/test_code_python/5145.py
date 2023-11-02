def solution():
    boys_percentage = 0.4
    boys_grade = 0.8
    girls_grade = 0.9

    # Calculate the average grade of boys
    boys_average = boys_percentage * boys_grade

    # Calculate the average grade of girls
    girls_average = (1 - boys_percentage) * girls_grade

    # Calculate the overall class average
    class_average = boys_average + girls_average
    result = class_average
    return result

print(solution())