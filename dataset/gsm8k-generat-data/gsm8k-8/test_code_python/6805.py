def solution():
    # Define the original prices
    iphone_price = 800
    iwatch_price = 300

    # Calculate the discounted prices
    iphone_discount = 0.15 * iphone_price
    iwatch_discount = 0.1 * iwatch_price

    iphone_price -= iphone_discount
    iwatch_price -= iwatch_discount

    # Calculate the total price
    total_price = iphone_price + iwatch_price

    # Apply the cashback discount
    cashback_discount = 0.02 * total_price
    total_price -= cashback_discount
    
    result = total_price
    return result

print(solution())