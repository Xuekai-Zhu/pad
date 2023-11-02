def solution():
    days_protesting = 4
    percent_increase = 25
    increase_amount = days_protesting * (percent_increase / 100)
    total_days = days_protesting + increase_amount
    result = total_days
    return result

print(solution())