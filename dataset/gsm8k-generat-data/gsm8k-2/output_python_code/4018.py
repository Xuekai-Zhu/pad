def solution():
    """The price per organic egg is 50 cents. The price of a tray of eggs that contains 30 eggs is $12. How much can you save, in cents, per egg if you buy a tray versus individual eggs?"""
    price_per_egg = 50
    eggs_per_tray = 30
    tray_price = 1200
    total_individual_price = eggs_per_tray * price_per_egg
    savings_per_egg = total_individual_price - tray_price
    result = savings_per_egg
    return result

print(solution())