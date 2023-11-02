def solution():
    iphone_price = 800  # iPhone 12 costs $800
    iwatch_price = 300  # iWatch costs $300

    iphone_discount = 0.15 * iphone_price  # 15% discount on iPhone
    iwatch_discount = 0.1 * iwatch_price  # 10% discount on iWatch

    total_discount = iphone_discount + iwatch_discount  # Total discount

    iphone_price -= iphone_discount  # Updated iPhone price after discount
    iwatch_price -= iwatch_discount  # Updated iWatch price after discount

    total_price = iphone_price + iwatch_price  # Total price before cashback

    cashback_discount = 0.02 * total_price  # 2% cashback discount

    total_price -= cashback_discount  # Total price after cashback discount

    result = total_price
    return result

print(solution())