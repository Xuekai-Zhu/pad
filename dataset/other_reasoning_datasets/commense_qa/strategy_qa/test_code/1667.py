def solution():
    number_of_theses = 95
    days_in_six_months = 182
    theses_per_day = number_of_theses / days_in_six_months
    if theses_per_day <= 0.5:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())