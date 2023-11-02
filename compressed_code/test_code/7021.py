def solution():
    
    sasha_muffins = 30
    melissa_muffins = sasha_muffins * 4
    total_muffins = sasha_muffins + melissa_muffins
    tiffany_muffins = total_muffins / 2
    muffin_price = 4
    sasha_contribution = sasha_muffins * muffin_price
    melissa_contribution = melissa_muffins * muffin_price
    tiffany_contribution = tiffany_muffins * muffin_price
    total_contribution = sasha_contribution + melissa_contribution + tiffany_contribution
    result = total_contribution
    return result

print(solution())