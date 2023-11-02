def solution():
    """Four years ago, Kody was only half as old as Mohamed. If Mohamed is currently twice 30 years old, how old is Kody?"""
    mohamed_age = 2 * 30 # Mohamed is currently twice 30 years old
    kody_age_4_years_ago = (1/2) * mohamed_age - 4 # Four years ago, Kody was only half as old as Mohamed
    kody_age = kody_age_4_years_ago + 4 # Add 4 years to Kody's age to get current age
    result = kody_age
    return result

print(solution())