def solution():
    first_month = 400
    second_month = first_month * 2
    total_months = 24
    total_kilometers = (first_month * (total_months // 2)) + (second_month * (total_months // 2))
    result = total_kilometers
    return result

print(solution())