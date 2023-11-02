def solution():
    
    
    
    betty_choc_chip = 4 * 12
    betty_oatmeal = 6 * 12
    betty_brownies = 2 * 12
    paige_sugar = 6 * 12
    paige_blondies = 3 * 12
    paige_cream_cheese = 5 * 12
    
    
    total_cookies_money = (betty_choc_chip + betty_oatmeal + paige_sugar) * 1
    total_brownies_money = (betty_brownies + paige_blondies + paige_cream_cheese) * 2
    total_money = total_cookies_money + total_brownies_money
    
    result = total_money
    return result

print(solution())