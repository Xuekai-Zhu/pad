def solution():
    """Mandy is ten years older than Jackson. Adele is 3/4 as old as Jackson. What's the total of their ages 10 years from now If Jackson is 20 years old now?"""
    jackson_age = 20
    mandy_age = jackson_age + 10
    adele_age = 0.75 * jackson_age
    total_age_in_10_years = jackson_age + 10 + mandy_age + 10 + adele_age + 10
    result = total_age_in_10_years
    return result

print(solution())