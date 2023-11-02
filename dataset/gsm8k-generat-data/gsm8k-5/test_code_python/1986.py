def solution():
    total_money = 240  # $240 was divided between Kelvin and Samuel
    samuel_share = (3/4) * total_money  # Samuel received 3/4 of the money
    spent_on_drinks = (1/5) * total_money  # Samuel spent 1/5 of the original $240 on drinks
    remaining_money = samuel_share - spent_on_drinks  # Samuel has remaining money after spending on drinks
    result = remaining_money
    return result

print(solution())