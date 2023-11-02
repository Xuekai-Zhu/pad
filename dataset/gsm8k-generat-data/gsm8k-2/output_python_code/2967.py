def solution():
    """Jon makes 3/4's the salary that Karen makes. John makes $3000 per month. How long will it take him to make the same amount of money that Karen does in 3 months?"""
    jon_salary = 3000
    karen_salary = (4/3) * jon_salary
    karen_salary_3_months = karen_salary * 3
    months_to_match_salary = karen_salary_3_months / jon_salary
    result = months_to_match_salary
    return result

print(solution())