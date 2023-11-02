def solution():
    """The price per organic egg is 50 cents. The price of a tray of eggs that contains 30 eggs is $12. How much can you save, in cents, per egg if you buy a tray versus individual eggs?"""
    # Define the price per egg and the price per tray
    EGG_PRICE = 0.5
    TRAY_PRICE = 12

    # Calculate the price per egg in a tray
    eggs_in_tray = 30
    price_per_egg_in_tray = TRAY_PRICE / eggs_in_tray

    # Calculate the savings per egg
    savings_per_egg = EGG_PRICE - price_per_egg_in_tray

    # Display the savings per egg
    result = int(savings_per_egg * 100)
    return result

print(solution())