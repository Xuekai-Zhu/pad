def solution():
    """After collecting all the old electronics in their house, Lauryn made $2000 from selling the items on eBay. 
    If her friend Aurelia also made 70% of what she sold on eBay after selling her used electronics, calculate the total amount of money the two friends made on eBay."""
    lauryn_money = 2000
    aurelia_percent = 0.7
    aurelia_money = lauryn_money * aurelia_percent
    total_money = lauryn_money + aurelia_money
    result = total_money
    
    return result

print(solution())