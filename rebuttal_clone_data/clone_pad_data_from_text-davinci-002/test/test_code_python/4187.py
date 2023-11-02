def solution():
    money_needed = 282
    money_saved = 42
    allowance = 24
    weeks_needed = (money_needed - money_saved) / allowance
    result = weeks_needed
    return result

print(solution())