def solution():
    """Twenty years ago, Shane was 2 times older than Garret is now. If Garret is currently 12, how old is Shane now?"""
    garret_age = 12
    shane_age_20_years_ago = 2 * garret_age
    shane_age_now = shane_age_20_years_ago + 20
    result = shane_age_now
    return result

print(solution())