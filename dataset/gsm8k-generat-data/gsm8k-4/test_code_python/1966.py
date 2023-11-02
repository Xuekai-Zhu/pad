def solution():
    """Selina is selling some of her old clothes to a second-hand store. They will buy her pants for $5 each, her shorts for $3 each, and her shirts for $4 each. She sells 3 pairs of pants, 5 pairs of shorts, and some shirts. After she gets her money, she sees 2 shirts that she likes which cost $10 each and buys them. She leaves the store with $30. How many shirts did she sell to the store?"""
    # Define the prices for each article of clothing
    PANTS_PRICE = 5
    SHORTS_PRICE = 3
    SHIRTS_PRICE = 4

    # Calculate the total amount earned from selling pants and shorts
    pants_total = 3 * PANTS_PRICE
    shorts_total = 5 * SHORTS_PRICE
    clothing_total = pants_total + shorts_total

    # Calculate the number of shirts sold
    money_earned = 30
    shirts_bought = 2
    shirts_cost = 10
    shirts_sold = (money_earned - (shirts_bought * shirts_cost) - clothing_total) / SHIRTS_PRICE

    # Return the result
    result = shirts_sold
    return result

print(solution())