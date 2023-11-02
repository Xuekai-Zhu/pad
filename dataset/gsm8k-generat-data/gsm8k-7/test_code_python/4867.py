def solution():
    # Calculate the price per apple in the first store
    price_per_apple_store1 = 3 / 6

    # Calculate the price per apple in the second store
    price_per_apple_store2 = 4 / 10

    # Calculate the savings per apple by buying from the second store
    savings_per_apple = price_per_apple_store1 - price_per_apple_store2

    # Convert savings to cents
    savings_per_apple_cents = savings_per_apple * 100

    result = savings_per_apple_cents
    return result

print(solution())