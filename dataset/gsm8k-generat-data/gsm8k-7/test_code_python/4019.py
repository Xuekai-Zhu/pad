def solution():
    price_per_egg = 0.5
    num_eggs_per_tray = 30
    cost_per_tray = 12

    # Calculate the cost per egg if buying a tray
    cost_per_egg_tray = cost_per_tray / num_eggs_per_tray

    # Calculate the savings per egg if buying a tray versus individual eggs
    savings_per_egg = price_per_egg - cost_per_egg_tray
    savings_in_cents = savings_per_egg * 100
    result = savings_in_cents
    return result

print(solution())