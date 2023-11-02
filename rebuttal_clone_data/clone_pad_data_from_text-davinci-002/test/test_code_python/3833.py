def solution():
    money_earned = 200
    money_spent_on_lunch = money_earned / 4
    money_spent_on_dvd = money_earned / 2
    money_left = money_earned - money_spent_on_lunch - money_spent_on_dvd
    result = money_left
    return result

print(solution())