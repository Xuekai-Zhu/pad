def solution():
    # Define the prices of coffee and cheesecake
    coffee_price = 6
    cheesecake_price = 10

    # Calculate the total price before discount
    total_price = coffee_price + cheesecake_price

    # Calculate the amount of the discount
    discount = total_price * 0.25

    # Calculate the final price after discount
    final_price = total_price - discount
    result = final_price
    return result

print(solution())