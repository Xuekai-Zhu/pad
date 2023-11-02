def solution():
    """Perry wants to buy a new modern bedroom set for $2000.  He received $200.00 in gift cards over the holidays that he can use toward the set.  The store is currently offering the entire set at 15% off.  If he signs up for the store credit card and uses it to buy the set, he will save an additional 10% off on the discounted set.  What is the final price of the set?"""
    # Define the price of the bedroom set and the discount percentages
    bedroom_set_price = 2000
    gift_card_amount = 200
    discount_percentage_1 = 0.15
    discount_percentage_2 = 0.1

    # Calculate the discounted price of the set after the first discount
    discounted_price_1 = bedroom_set_price * (1 - discount_percentage_1)

    # Calculate the discounted price of the set after the second discount
    discounted_price_2 = discounted_price_1 * (1 - discount_percentage_2)

    # Calculate the final price of the set after applying the gift card
    final_price = discounted_price_2 - gift_card_amount

    # Display the final price of the set
    result = final_price
    return result

print(solution())