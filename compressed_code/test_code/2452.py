def solution():
    
    total_cost = 500
    birthday_money = 200
    christmas_money = 150
    amount_left = total_cost - birthday_money - christmas_money
    games_needed = int(amount_left / 7.5)
    result = games_needed
    return result

print(solution())