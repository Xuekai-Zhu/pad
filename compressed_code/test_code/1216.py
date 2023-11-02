def solution():
    
    sasha_muffins = 30
    melissa_muffins = 4 * sasha_muffins
    total_muffins = sasha_muffins + melissa_muffins
    tiffany_muffins = total_muffins / 2
    total_money = (sasha_muffins + melissa_muffins + tiffany_muffins) * 4
    result = total_money
    return result

print(solution())