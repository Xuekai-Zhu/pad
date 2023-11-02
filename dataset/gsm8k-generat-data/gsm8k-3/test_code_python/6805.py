def solution():
    """Dexter went to the mall and saw that Apple products are on sale. He wants to buy an iPhone 12 with a 15% discount and an iWatch with a 10% discount. The price tag shows that an iPhone 12 costs $800 while an iWatch costs $300. Upon check out, he will receive a further 2% cashback discount. How much would the items cost in total after the discount and cashback?"""
    # Define the prices and discount rates
    IPHONE_PRICE = 800
    IPHONE_DISCOUNT = 0.15
    IWATCH_PRICE = 300
    IWATCH_DISCOUNT = 0.1
    CASHBACK_DISCOUNT = 0.02

    # Calculate the discounted prices
    iphone_discounted_price = IPHONE_PRICE * (1-IPHONE_DISCOUNT)
    iwatch_discounted_price = IWATCH_PRICE * (1-IWATCH_DISCOUNT)

    # Calculate the total cost before cashback
    total_cost_before_cashback = iphone_discounted_price + iwatch_discounted_price

    # Calculate the cashback amount
    cashback_amount = total_cost_before_cashback * CASHBACK_DISCOUNT

    # Calculate the total cost after cashback
    total_cost = total_cost_before_cashback - cashback_amount

    # Display the total cost
    result = total_cost
    return result

print(solution())