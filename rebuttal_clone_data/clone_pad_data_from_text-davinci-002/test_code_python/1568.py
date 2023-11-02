def solution():
    sasha_muffins = 30
    melissa_muffins = sasha_muffins * 4
    tiffany_muffins = (sasha_muffins + melissa_muffins) / 2
    muffins_total = sasha_muffins + melissa_muffins + tiffany_muffins
    price_per_muffin = 4
    money_contributed = muffins_total * price_per_muffin
    result = money_contributed
    return result

print(solution())