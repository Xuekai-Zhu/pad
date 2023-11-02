def solution():
    """Kat gets a 95% on her first math test and an 80% on her second math test. If she wants an average grade of at least 90% in her math class, what does she need to get on her third final math test?"""
    current_average = (95 + 80) / 2
    desired_average = 90
    third_test_needed = (desired_average * 3) - (95 + 80)
    result = third_test_needed
    return result

print(solution())