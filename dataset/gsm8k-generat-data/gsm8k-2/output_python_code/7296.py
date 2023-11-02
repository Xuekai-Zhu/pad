def solution():
    """After collecting all the old electronics in their house, Lauryn made $2000 from selling the items on eBay. If her friend Aurelia also made 70% of what she sold on eBay after selling her used electronics, calculate the total amount of money the two friends made on eBay."""
    lauryn_earnings = 2000
    aurelia_percentage = 0.7
    aurelia_earnings = lauryn_earnings * aurelia_percentage
    total_earnings = lauryn_earnings + aurelia_earnings
    result = total_earnings
    return result

print(solution())