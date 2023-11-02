def solution():
    """Five years ago, the sum of Sebastian's age and his sister's age was 3/4 of their father's age. How old is their father today if Sebastian is 40 years old and 10 years older than his sister?"""
    sebastian_age = 40
    sister_age = sebastian_age - 10
    total_age_5_years_ago = (sebastian_age - 5) + (sister_age - 5)
    father_age_5_years_ago = (4 / 3) * total_age_5_years_ago
    father_age = father_age_5_years_ago + 5 * 3
    result = father_age
    return result

print(solution())