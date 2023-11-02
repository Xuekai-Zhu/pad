def solution():
    
    gina_money = 400
    mom_money = gina_money / 4
    clothes_money = gina_money / 8
    charity_money = gina_money / 5

    remaining_money = gina_money - mom_money - clothes_money - charity_money

    result = remaining_money
    return result

print(solution())