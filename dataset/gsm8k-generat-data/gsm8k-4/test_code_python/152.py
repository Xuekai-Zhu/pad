def solution():
    """A one-year subscription to a newspaper is offered with a 45% discount. How much does the discounted subscription cost if a subscription normally costs $80?"""
    # Define the original price of the subscription
    original_price = 80

    # Calculate the discount
    discount = original_price * 0.45

    # Calculate the final price with the discount applied
    final_price = original_price - discount

    result = final_price
    return result

print(solution())