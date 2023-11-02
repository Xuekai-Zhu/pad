def solution():
    """Arman is six times older than his sister. His sister is 2 years old four years ago. In how many years will Arman's age be 40?"""
    sister_age_now = 2 + 4  # 6 years old
    arman_age_now = 6 * sister_age_now
    years_to_40 = 40 - arman_age_now
    result = years_to_40
    return result

print(solution())