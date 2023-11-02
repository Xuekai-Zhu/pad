def solution():
    prices = [7.5, 10, 8.5, 9]  # Prices of the sundaes ordered
    total_price = sum(prices)  # Total price before tip
    tip = 0.2 * total_price  # Tip amount
    final_bill = total_price + tip  # Total bill including tip
    result = final_bill
    return result

print(solution())