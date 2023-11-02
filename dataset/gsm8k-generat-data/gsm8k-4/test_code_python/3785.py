def solution():
    """Kat gets a 95% on her first math test and an 80% on her second math test. If she wants an average grade of at least 90% in her math class, what does she need to get on her third final math test?"""
    # Define the desired average grade and the weights of each grade
    desired_average = 90
    weight_first = 0.3
    weight_second = 0.3
    weight_third = 0.4

    # Define the grades received on the first two tests
    grade_first = 95
    grade_second = 80

    # Calculate the grade needed on the third test to achieve the desired average
    grade_third = (desired_average - (grade_first*weight_first) - (grade_second*weight_second)) / weight_third

    # Return the result
    result = round(grade_third)
    return result

print(solution())