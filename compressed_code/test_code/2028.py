def solution():
    
    january_income = 4000
    february_income = 2 * january_income
    march_income = february_income - 2000
    total_income = january_income + february_income + march_income
    result = total_income
    return result

print(solution())