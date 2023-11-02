def solution():
    total_cost = 800
    phone_tradein = 240
    weekly_earnings = 80
    money_needed = total_cost - phone_tradein
    number_of_weeks = money_needed / weekly_earnings
    result = number_of_weeks
    return result

print(solution())