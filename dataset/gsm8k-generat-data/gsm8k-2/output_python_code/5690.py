def solution():
    """To celebrate a recent promotion, Arthur decided to treat himself to dinner at a nice restaurant. He ordered a nice appetizer for $8, a delicious ribeye steak for his entrée at $20, had two glasses of nice red wine with dinner for $3 each, and a slice of caramel cheesecake for dessert for $6. He used a voucher for half off the price of his entrée, but he very thoughtfully tipped his waitress a full 20% of what the full cost of his meal would have been without the discount. How much, including the tip, did Arthur spend on dinner?"""
    appetizer_price = 8
    steak_price = 20
    wine_price = 3
    dessert_price = 6
    entrée_discount = 0.5
    tax_rate = 0.08
    tip_rate = 0.2

    full_cost = (appetizer_price + (2 * wine_price) + dessert_price + steak_price)

    discounted_cost = full_cost * (1 - entrée_discount)
    total_cost = discounted_cost * (1 + tax_rate)
    tip_amount = full_cost * tip_rate

    result = total_cost + tip_amount
    return result

print(solution())