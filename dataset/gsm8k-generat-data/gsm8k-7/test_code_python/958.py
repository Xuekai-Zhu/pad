def solution():
    djibo_age = 17
    sum_5_years_ago = 35 - 10  # 10 years ago the sum was 35 - 10 = 25
    sister_age_5_years_ago = sum_5_years_ago - djibo_age
    sister_age_today = sister_age_5_years_ago + 5  # Add 5 years to get the present age
    result = sister_age_today
    return result

print(solution())