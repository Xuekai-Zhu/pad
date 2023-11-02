def solution():
    """Brittany got a 78 on her first test. After her second test, her average rose to an 81. What grade did she get on her second test?"""
    # Define the initial grade and the desired average
    initial_grade = 78
    desired_average = 81

    # Calculate the score needed on the second test to achieve the desired average
    second_test_grade = (desired_average * 2) - initial_grade

    # Return the result
    result = second_test_grade
    return result

print(solution())