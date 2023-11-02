def solution():
    # Calculate the set price after 15% discount
    set_price = 2000 * 0.85

    # Calculate the price after additional 10% discount with store credit card
    final_price = set_price * 0.9

    # Subtract the gift card value from the final price
    final_price -= 200

    result = final_price
    return result

print(solution())