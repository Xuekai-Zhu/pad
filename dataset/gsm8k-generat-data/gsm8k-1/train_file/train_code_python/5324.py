def solution():
    """After five years, Ron will be four times as old as Maurice. If Ron's age now is 43, how old is Maurice now?"""
    ron_age_after_5_years = 48 # 43 + 5
    ratio_of_ages = 4
    total_ratio = 5  # 4 + 1
    maurice_age_after_5_years = ron_age_after_5_years / ratio_of_ages
    maurice_age_now = maurice_age_after_5_years - 5
    result = maurice_age_now
    return result

print(solution())