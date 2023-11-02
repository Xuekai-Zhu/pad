def solution():
    """Darrell and Allen's ages are in the ratio of 7:11. If their total age now is 162, calculate Allen's age 10 years from now."""
    total_age = 162
    age_ratio = 7/11
    allen_age = total_age / (age_ratio + 1)
    allen_age_10_years = allen_age + 10
    result = allen_age_10_years
    return result

print(solution())