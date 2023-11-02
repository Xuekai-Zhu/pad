def solution():
    """John buys 1/2 gallon jugs of cold brew coffee every 4 days. How many cups of coffee does he drink a day?"""
    # Define the amount of coffee in a half gallon jug
    HALF_GALLON = 64 # 1 gallon = 128 oz, 1/2 gallon = 64 oz

    # Calculate the amount of coffee John drinks in a day
    cups_per_day = HALF_GALLON / 4 / 8 # 1 jug every 4 days, 8 oz per cup

    # Display the number of cups John drinks per day
    result = cups_per_day
    return result

print(solution())