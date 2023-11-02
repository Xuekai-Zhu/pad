def solution():
    coffee_price = 6  # Price of one cup of coffee
    cheesecake_price = 10  # Price of one piece of cheesecake
    discount = 0.25  # 25% discount on the total price

    # Calculate the total price before discount
    total_price = coffee_price + cheesecake_price

    # Calculate the discount amount
    discount_amount = total_price * discount

    # Calculate the final price after discount
    final_price = total_price - discount_amount
    result = final_price
    return result

print(solution())