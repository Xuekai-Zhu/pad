def solution():
    """Kat gets a 95% on her first math test and an 80% on her second math test. If she wants an average grade of at least 90% in her math class, what does she need to get on her third final math test?"""
    # Define the current average and the desired average
    current_average = (95 + 80) / 2
    desired_average = 90

    # Calculate the minimum score needed on the final test
    min_score = (desired_average * 3) - (95 + 80)

    result = min_score
    return result

print(solution())