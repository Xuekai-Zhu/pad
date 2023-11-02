def solution():
    """Four years ago, Kody was only half as old as Mohamed. If Mohamed is currently twice 30 years old, how old is Kody?"""
    # Define Mohamed's current age
    mohamed_age = 2 * 30

    # Calculate Mohamed's age 4 years ago
    mohamed_age_4years_ago = mohamed_age - 4

    # Calculate Kody's age 4 years ago
    kody_age_4years_ago = mohamed_age_4years_ago / 2

    # Calculate Kody's current age
    kody_age = kody_age_4years_ago + 4

    result = kody_age
    return result

print(solution())