def solution():
    """Jean is two years older than Mark. Two years ago Mark was 5 years older than half Jan's age. If Jan is 30 how old is Jean?"""
    jan_age = 30
    half_jan_age_two_years_ago = (jan_age - 2) / 2
    mark_age_two_years_ago = half_jan_age_two_years_ago + 5
    mark_age = mark_age_two_years_ago + 2
    jean_age = mark_age + 2
    result = jean_age
    return result

print(solution())