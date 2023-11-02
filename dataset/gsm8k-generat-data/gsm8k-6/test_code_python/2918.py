def solution():
    # Calculate the total amount Monica will make from the party
    original_price = 25 * 20  # $25.00 per person for 20 guests
    discount = 0.1 * original_price  # 10% discount for repeat customer
    final_price = original_price - discount  # price after discount
    result = final_price
    return result

print(solution())