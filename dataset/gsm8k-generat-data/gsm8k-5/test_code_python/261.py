def solution():
    price_orange = 0.5  # Price of one orange
    total_fruits = 36  # Total number of fruits bought
    apples_ratio = 1/4  # Ratio of apples to watermelons
    watermelon_ratio = 1 - apples_ratio  # Ratio of watermelons to apples

    # Calculate the number of each fruit bought
    apples = total_fruits * apples_ratio
    watermelons = total_fruits * watermelon_ratio
    oranges = total_fruits - apples - watermelons

    # Calculate the total cost of the fruits
    total_cost = oranges * price_orange + apples * price_apple + watermelons * price_watermelon
    # We don't know the price of apple or watermelon yet, so let's call it x

    # We know the total bill was $66
    # So, total cost = total bill = $66
    # And, total cost = 36 * x    (since we bought 36 fruits)
    # Therefore, x = total cost / 36 = $66 / 36
    price_apple = price_watermelon = total_cost / 36

    result = price_apple
    return result

print(solution())