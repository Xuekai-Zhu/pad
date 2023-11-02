def solution():
    """James made $4000 in January. The next month he made twice as much. In March, however, James made $2000 less than in February. How much has James made so far this year?"""
    # Define the income for each month
    january_income = 4000
    february_income = january_income * 2
    march_income = february_income - 2000

    # Calculate the total income for the year
    total_income = january_income + february_income + march_income

    # return the result
    result = total_income
    return result

print(solution())