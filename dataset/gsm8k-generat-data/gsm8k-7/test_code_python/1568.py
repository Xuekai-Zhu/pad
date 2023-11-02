def solution():
    sasha_muffins = 30
    melissa_muffins = sasha_muffins * 4
    total_muffins = sasha_muffins + melissa_muffins
    tiffany_muffins = total_muffins / 2
    
    # Calculate the total amount of money contributed
    total_money = (sasha_muffins + melissa_muffins + tiffany_muffins) * 4

    # Calculate the amount of money contributed by each person
    sasha_money = sasha_muffins * 4
    melissa_money = melissa_muffins * 4
    tiffany_money = tiffany_muffins * 4
    
    result = sasha_money, melissa_money, tiffany_money
    return result

print(solution())