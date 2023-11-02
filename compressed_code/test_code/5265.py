def solution():
    
    bracelets_made = 52
    materials_cost = 3.00
    bracelets_given_away = 8
    remaining_bracelets = bracelets_made - bracelets_given_away
    price_per_bracelet = 0.25
    total_earned = remaining_bracelets * price_per_bracelet
    profit = total_earned - materials_cost
    result = profit
    return result

print(solution())