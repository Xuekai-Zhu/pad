def solution():
    apple_price_per_dozen = (7 / 2) - (1 / 12)  # Tony paid $7 for 2 dozen apples, so we subtract the cost of 1 dozen apples
    banana_price = 7 - (2 * apple_price_per_dozen) - 5 + apple_price_per_dozen  # Subtract the cost of apples and Arnold's payment to get the cost of the bananas
    result = banana_price
    return result

print(solution())