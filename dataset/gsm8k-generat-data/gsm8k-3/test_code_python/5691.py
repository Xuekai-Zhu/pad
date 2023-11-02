def solution():
    """To celebrate a recent promotion, Arthur decided to treat himself to dinner at a nice restaurant. He ordered a nice appetizer for $8, a delicious ribeye steak for his entrée at $20, had two glasses of nice red wine with dinner for $3 each, and a slice of caramel cheesecake for dessert for $6. 
    He used a voucher for half off the price of his entrée, but he very thoughtfully tipped his waitress a full 20% of what the full cost of his meal would have been without the discount. How much, including the tip, did Arthur spend on dinner?"""
    # Define the prices of each menu item
    APPETIZER_PRICE = 8
    STEAK_PRICE = 20
    WINE_PRICE = 3
    DESSERT_PRICE = 6

    # Calculate the cost of Arthur's meal without the discount
    full_price = APPETIZER_PRICE + STEAK_PRICE + 2*WINE_PRICE + DESSERT_PRICE

    # Calculate the cost of Arthur's meal with the discount
    discount_price = full_price - (STEAK_PRICE/2)

    # Calculate the tip based on the full price
    tip = 0.2 * full_price

    # Calculate the total cost including the tip
    total_cost = discount_price + tip

    # Display the total cost
    result = total_cost
    return result

print(solution())