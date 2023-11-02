def solution():
    """James made $4000 in January. The next month he made twice as much. In March, however, James made $2000 less than in February. How much has James made so far this year?"""
    january_income = 4000
    february_income = 2 * january_income
    march_income = february_income - 2000
    total_income = january_income + february_income + march_income
    result = total_income
    return result

print(solution())