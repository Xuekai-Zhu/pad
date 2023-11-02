def solution():
    """The price per organic egg is 50 cents. The price of a tray of eggs that contains 30 eggs is $12. How much can you save, in cents, per egg if you buy a tray versus individual eggs?"""
    # Define the price per egg and the price per tray
    egg_price = 0.5
    tray_price = 12

    # Calculate the price per egg if you buy a tray
    eggs_per_tray = 30
    price_per_tray = tray_price / eggs_per_tray
    price_per_egg_tray = price_per_tray / egg_price

    # Calculate the price per egg if you buy individual eggs
    price_per_egg_individual = 1

    # Calculate the savings per egg if you buy a tray
    savings_per_egg = (price_per_egg_individual - price_per_egg_tray) * 100

    result = savings_per_egg
    return result

print(solution())