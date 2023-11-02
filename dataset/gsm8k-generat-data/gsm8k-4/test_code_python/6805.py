def solution():
    """Dexter went to the mall and saw that Apple products are on sale. He wants to buy an iPhone 12 with a 15% discount and an iWatch with a 10% discount. The price tag shows that an iPhone 12 costs $800 while an iWatch costs $300. Upon check out, he will receive a further 2% cashback discount. How much would the items cost in total after the discount and cashback?"""
    # Define the prices of iPhone 12 and iWatch
    iphone_price = 800
    iwatch_price = 300

    # Calculate the discounts for iPhone 12 and iWatch
    iphone_discount = iphone_price * 0.15
    iwatch_discount = iwatch_price * 0.1

    # Calculate the discounted prices for iPhone 12 and iWatch
    iphone_discounted_price = iphone_price - iphone_discount
    iwatch_discounted_price = iwatch_price - iwatch_discount

    # Calculate the total price after discount
    total_price = iphone_discounted_price + iwatch_discounted_price

    # Calculate the cashback discount
    cashback_discount = total_price * 0.02

    # Calculate the final price after cashback
    final_price = total_price - cashback_discount

    result = final_price
    return result

print(solution())