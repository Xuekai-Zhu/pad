def solution():
    taco_price_soft = 2
    taco_price_hard = 5
    tacos_bought_family = 4 + 3
    tacos_bought_others = 10 * 2
    total_tacos_sold = tacos_bought_family + tacos_bought_others
    total_price = (tacos_bought_family * taco_price_hard) + (tacos_bought_others * taco_price_soft)
    result = total_price
    return result

print(solution())