def solution():
    # Calculate the price per apple for the first store
    price_per_apple_1 = 3 / 6  # $3 for 6 apples

    # Calculate the price per apple for the second store
    price_per_apple_2 = 4 / 10  # $4 for 10 apples

    # Calculate the difference in price per apple between the two stores
    price_difference = price_per_apple_1 - price_per_apple_2

    # Convert the price difference to cents
    cents_saved_per_apple = price_difference * 100
    result = cents_saved_per_apple
    return result

print(solution())