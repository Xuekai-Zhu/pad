def solution():
    """Shiloh is 44 years old today. In 7 years, he will be three times as old as his nephew. How old is his nephew today?"""
    shiloh_age = 44
    nephew_age_in_7_years = (shiloh_age + 7) / 3
    nephew_age_today = nephew_age_in_7_years - 7
    result = nephew_age_today
    return result

print(solution())