def solution():
    """In a restaurant, one cup of coffee is $6 and a piece of cheesecake $10. When buying them together, the client gets a 25% discount. What is the final price of such a set?"""
    coffee_price = 6
    cheesecake_price = 10
    discount_percent = 25
    total_price = coffee_price + cheesecake_price
    discount_amount = total_price * (discount_percent / 100)
    final_price = total_price - discount_amount
    result = final_price
    return result

print(solution())