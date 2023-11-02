def solution():
    # Calculate how much money Samuel received and how much he spent on drinks
    samuel_money = (3/4) * 240  # Samuel received 3/4 of the $240
    money_spent_on_drinks = (1/5) * 240  # Samuel spent 1/5 of the original $240 on drinks
    money_left = samuel_money - money_spent_on_drinks  # Calculate how much money Samuel has left
    
    result = money_left
    return result

print(solution())