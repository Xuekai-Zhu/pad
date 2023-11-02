def solution():
    ken_oz = 700
    ken_price = 40
    nich_oz = 6 * ken_oz

    # Calculate the total price paid by Kenneth
    ken_total_price = ken_oz * ken_price

    # Calculate the total price paid by Nicholas
    nich_total_price = nich_oz * ken_price

    # Calculate the difference in price paid by Nicholas and Kenneth
    price_diff = nich_total_price - ken_total_price
    result = price_diff
    return result

print(solution())