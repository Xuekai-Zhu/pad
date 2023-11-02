def solution():
    """Jerry is twice as old as he was 5 years ago. How old will Jerry be in 3 years?"""
    jerry_age_5_years_ago = 0.5 * jerry_age_current - 5
    jerry_age_in_3_years = jerry_age_current + 3
    result = jerry_age_in_3_years
    return result

print(solution())