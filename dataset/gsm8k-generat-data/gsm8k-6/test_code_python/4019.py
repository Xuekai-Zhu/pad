def solution():
    # Calculate the price per egg in a tray
    price_per_egg = 12 / 30  # price of a tray of 30 eggs is $12

    # Calculate the saving per egg when buying a tray
    saving_per_egg = 50 - price_per_egg*100  # convert price per egg to cents
    result = saving_per_egg
    return result

print(solution())