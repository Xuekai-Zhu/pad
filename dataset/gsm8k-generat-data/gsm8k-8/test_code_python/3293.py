def solution():
    # Define the total number of tests and the desired average grade
    total_tests = 4
    desired_average = 85

    # Calculate Carl's current average grade
    current_average = (80 + 75 + 90) / 3

    # Calculate the minimum grade Carl needs on his fourth test to achieve the desired average
    # grade for the class
    min_grade = (desired_average * total_tests) - (80 + 75 + 90)

    result = min_grade
    return result

print(solution())