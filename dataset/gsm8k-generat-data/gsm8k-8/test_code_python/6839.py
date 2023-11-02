def solution():
    money_earned = 200
    money_spent_on_lunch = money_earned * (1/4)
    money_spent_on_DVD = money_earned * (1/2)
    money_left = money_earned - money_spent_on_lunch - money_spent_on_DVD
    result = money_left
    return result

print(solution())