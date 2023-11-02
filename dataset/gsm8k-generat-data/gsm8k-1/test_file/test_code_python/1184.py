def solution():
    """Digimon had its 20th anniversary. When it came out John was twice as old as Jim. If John is 28 now, how old is Jim?"""
    years_ago = 20
    john_age_then = years_ago * 2
    jim_age_then = john_age_then / 2
    jim_age_now = jim_age_then + years_ago
    result = jim_age_now
    return result

print(solution())