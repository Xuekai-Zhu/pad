def solution():
    """Trip wanted to watch the new action movie in theaters. An evening ticket cost $10 and a large popcorn & drink combo would cost him an additional $10. He noticed on their website, they had a special offer. From 12 noon to 3 pm, save 20% off tickets and 50% off any food combos. How much money could Trip save by going to the earlier movie?"""
    # Define the prices of evening ticket and combo
    evening_ticket_price = 10
    combo_price = 10

    # Calculate the prices with the discount
    discount_ticket_price = evening_ticket_price * 0.8
    discount_combo_price = combo_price * 0.5

    # Calculate the total price of attending the movie with the discounts
    total_price_discount = discount_ticket_price + discount_combo_price

    # Calculate the total amount saved by using the discount
    total_savings = evening_ticket_price + combo_price - total_price_discount

    # Return the total amount saved
    result = total_savings
    return result

print(solution())