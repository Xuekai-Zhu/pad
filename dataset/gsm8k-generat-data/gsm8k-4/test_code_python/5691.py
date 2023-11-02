def solution():
    """To celebrate a recent promotion, Arthur decided to treat himself to dinner at a nice restaurant. He ordered a nice appetizer for $8, a delicious ribeye steak for his entrée at $20, had two glasses of nice red wine with dinner for $3 each, and a slice of caramel cheesecake for dessert for $6. He used a voucher for half off the price of his entrée, but he very thoughtfully tipped his waitress a full 20% of what the full cost of his meal would have been without the discount. How much, including the tip, did Arthur spend on dinner?"""
    # Define the prices of the appetizer, entrée, wine, and dessert
    appetizer_price = 8
    entrée_price = 20
    wine_price = 3
    dessert_price = 6

    # Calculate the total cost of the meal before the discount and tip
    total_cost_before_discount = appetizer_price + entrée_price + (2 * wine_price) + dessert_price

    # Calculate the cost of the entrée after the discount
    entrée_discount = 0.5 * entrée_price

    # Calculate the total cost of the meal after the discount and before the tip
    total_cost_after_discount = appetizer_price + entrée_discount + (2 * wine_price) + dessert_price

    # Calculate the total cost of the meal after the discount and including the tip
    total_cost_with_tip = total_cost_after_discount * 1.2

    result = total_cost_with_tip
    return result

print(solution())