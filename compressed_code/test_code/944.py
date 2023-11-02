def solution():
    

    total_money = 200
    sheet_cost = 42
    rope_cost = 18
    propane_cost = 14
    helium_cost_per_ounce = 1.5

    
    money_left = total_money - sheet_cost - rope_cost - propane_cost

    
    max_helium_ounces = money_left / helium_cost_per_ounce

    
    max_height = max_helium_ounces * 113

    result = max_height
    return result

print(solution())