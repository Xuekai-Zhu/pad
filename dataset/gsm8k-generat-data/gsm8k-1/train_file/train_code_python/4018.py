def solution():
    """The price per organic egg is 50 cents. The price of a tray of eggs that contains 30 eggs is $12. How much can you save, in cents, per egg if you buy a tray versus individual eggs?"""
    price_per_egg = 0.5
    eggs_per_tray = 30
    price_per_tray = 12
    price_per_tray_per_egg = price_per_tray / eggs_per_tray
    savings_per_egg = price_per_egg - price_per_tray_per_egg
    result = savings_per_egg * 100
    return result

print(solution())