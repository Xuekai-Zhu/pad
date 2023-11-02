def solution():
    """In a restaurant, one cup of coffee is $6 and a piece of cheesecake $10. When buying them together, the client gets a 25% discount. What is the final price of such a set?"""
    # Define the prices of coffee and cheesecake
    coffee_price = 6
    cheesecake_price = 10

    # Calculate the total price without discount
    total_price = coffee_price + cheesecake_price

    # Calculate the discount amount
    discount = total_price * 0.25

    # Calculate the final price with discount
    final_price = total_price - discount

    # return the result
    result = final_price
    return result

print(solution())