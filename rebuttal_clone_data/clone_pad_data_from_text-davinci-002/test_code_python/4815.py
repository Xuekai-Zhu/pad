def solution():
    bracelets_ sold = 30
    total_money = 60
    bracelets_for_5 = bracelets_sold - (total_money / 5)
    bracelets_for_8 = bracelets_for_5 / 2
    total_money = (bracelets_for_5 * 5) + (bracelets_for_8 * 8)
    result = total_money
    
    return result

print(solution())