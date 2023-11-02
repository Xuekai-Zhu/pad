def solution():
    """Kat gets a 95% on her first math test and an 80% on her second math test. If she wants an average grade of at least 90% in her math class, what does she need to get on her third final math test?"""
    current_grade = (95 + 80) / 2
    desired_grade = 90
    percent_needed = (desired_grade - current_grade) / (100 - current_grade) * 100
    result = percent_needed
    return result

print(solution())