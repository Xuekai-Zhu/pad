def solution():
    # Calculate the price per apple at each store
    price_per_apple_store1 = 3 / 6
    price_per_apple_store2 = 4 / 10

    # Calculate the difference in price per apple
    price_difference = price_per_apple_store1 - price_per_apple_store2

    # Convert the price difference to cents and round to the nearest cent
    cents_saved_per_apple = round(price_difference * 100)

    result = cents_saved_per_apple
    return result

print(solution())