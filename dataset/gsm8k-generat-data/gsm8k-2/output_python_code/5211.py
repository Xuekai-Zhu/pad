def solution():
    """Four years ago, Kody was only half as old as Mohamed. If Mohamed is currently twice 30 years old, how old is Kody?"""
    mohamed_current_age = 2*30
    kody_age_four_years_ago = mohamed_current_age / 2 - 4
    kody_current_age = kody_age_four_years_ago + 4
    result = kody_current_age
    return result

print(solution())