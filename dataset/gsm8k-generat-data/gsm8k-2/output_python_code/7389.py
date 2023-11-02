def solution():
    """Today is my birthday and I'm three times older than I was six years ago. What is my age?"""
    age_six_years_ago = x
    age_today = age_six_years_ago + 6
    if age_today == 3 * age_six_years_ago:
        result = age_today
        return result

print(solution())