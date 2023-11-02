def solution():
    # Calculate the price per egg in the tray
    price_per_egg = 12 / 30

    # Calculate the difference between the price per egg in the tray and the individual price
    savings_per_egg = 0.5 - price_per_egg

    # Convert the savings to cents
    savings_per_egg_in_cents = savings_per_egg * 100
    result = savings_per_egg_in_cents
    return result

print(solution())