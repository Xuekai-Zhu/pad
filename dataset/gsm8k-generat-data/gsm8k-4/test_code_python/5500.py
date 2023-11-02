def solution():
    """Perry wants to buy a new modern bedroom set for $2000. He received $200.00 in gift cards over the holidays that he can use toward the set. The store is currently offering the entire set at 15% off. If he signs up for the store credit card and uses it to buy the set, he will save an additional 10% off on the discounted set. What is the final price of the set?"""
    # Define the initial price and the discount percentages
    initial_price = 2000
    gift_card = 200
    discount1 = 0.15
    discount2 = 0.10

    # Calculate the discounted price after the first discount
    discounted_price1 = initial_price * (1 - discount1)

    # Calculate the final price after the second discount and using the gift cards
    final_price = (discounted_price1 * (1 - discount2)) - gift_card

    result = final_price
    return result

print(solution())