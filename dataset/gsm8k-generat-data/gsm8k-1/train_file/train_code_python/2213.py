def solution():
    """Matt did his homework for 150 minutes. He spent 30% of that time on math and 40% on science. He spent the remaining time on other subjects. How much time did Matt spend on homework in other subjects?"""
    total_time = 150
    math_time = total_time * 0.3
    science_time = total_time * 0.4
    other_subjects_time = total_time - math_time - science_time
    result = other_subjects_time
    return result

print(solution())