def solution():
    mowing_rate = 14
    hours_mowed = 2
    days_mowed = 7
    total_earnings = mowing_rate * hours_mowed * days_mowed
    shoes_cost = total_earnings / 2
    money_left = total_earnings - shoes_cost
    result = money_left
    return result

print(solution())