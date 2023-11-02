def solution():
    # Calculate the price of the shoes after the 30% discount
    shoes_price = 200 * 0.7

    # Calculate the total price of the shirts
    shirts_price = 2 * 80

    # Calculate the total price before the additional 5% discount
    total_price = shoes_price + shirts_price

    # Calculate the final price after the additional 5% discount
    final_price = total_price * 0.95
    result = final_price
    return result

print(solution())