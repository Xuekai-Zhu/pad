def solution():
    sister_age_4_years_ago = 2
    sister_age_today = sister_age_4_years_ago + 4

    arman_age_today = 6 * sister_age_today

    years_needed = 40 - arman_age_today

    result = years_needed
    return result

print(solution())