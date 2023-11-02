def solution():
    price_per_egg = 50  # Price per organic egg in cents
    tray_price = 1200  # Price of a tray of eggs in cents ($12)

    # Calculate the price per egg in a tray
    price_per_tray_egg = tray_price / 30

    # Calculate the savings per egg when buying a tray instead of individual eggs
    savings_per_egg = price_per_egg - price_per_tray_egg
    result = savings_per_egg
    return result

print(solution())