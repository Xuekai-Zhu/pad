def solution():
    coffee_price = 6  # price of one cup of coffee
    cheesecake_price = 10  # price of one piece of cheesecake
    discount = 0.25  # 25% discount
    total_price = coffee_price + cheesecake_price  # total price without discount
    discount_amount = discount * total_price  # discount amount
    final_price = total_price - discount_amount  # final price with discount
    result = final_price
    return result

print(solution())