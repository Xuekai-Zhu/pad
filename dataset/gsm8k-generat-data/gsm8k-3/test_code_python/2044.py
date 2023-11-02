def solution():
    """Twenty years ago, Shane was 2 times older than Garret is now. If Garret is currently 12, how old is Shane now?"""
    # Let's first find out Shane's age twenty years ago
    shane_twenty_years_ago = 2 * (12 - 20) # Garret is currently 12, so twenty years ago he was 12 - 20 = -8 years old
    # Therefore, Shane was 2 times older than Garret twenty years ago, so shane_twenty_years_ago = 2 * garret_twenty_years_ago

    # Now we can find out Shane's current age by adding 20 years to shane_twenty_years_ago
    shane_age_now = shane_twenty_years_ago + 20

    # Display Shane's current age
    result = shane_age_now
    return result

print(solution())