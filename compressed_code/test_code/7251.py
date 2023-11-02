def solution():
    
    rock_and_roll_price = 5
    pop_price = 10
    dance_price = 3
    country_price = 7
    
    rock_and_roll_cds = 4
    pop_cds = 4
    dance_cds = 4
    country_cds = 4
    
    total_cost = (rock_and_roll_price * rock_and_roll_cds) + (pop_price * pop_cds) + (dance_price * dance_cds) + (country_price * country_cds)
    
    money_short = total_cost - 75
    
    result = money_short
    return result

print(solution())