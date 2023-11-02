def solution():
    # Convert milliliters to liters
    milk_750_ml = 750 / 1000  # 750 milliliters = 0.75 liters
    milk_250_ml = 250 / 1000  # 250 milliliters = 0.25 liters

    # Total volume of milk in liters
    total_milk = 2 + milk_750_ml + milk_250_ml
    result = total_milk
    return result

print(solution())