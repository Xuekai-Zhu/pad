def solution():
    initial_value = 100
    six_months_value = initial_value - (initial_value * 0.25)
    one_year_value = six_months_value - (six_months_value * 0.20)
    result = round(one_year_value, 2)
    return result

print(solution())