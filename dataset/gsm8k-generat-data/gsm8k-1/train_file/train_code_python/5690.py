def solution():
    """To celebrate a recent promotion, Arthur decided to treat himself to dinner at a nice restaurant. He ordered a nice appetizer for $8, a delicious ribeye steak for his entrée at $20, had two glasses of nice red wine with dinner for $3 each, and a slice of caramel cheesecake for dessert for $6. He used a voucher for half off the price of his entrée, but he very thoughtfully tipped his waitress a full 20% of what the full cost of his meal would have been without the discount. How much, including the tip, did Arthur spend on dinner?"""
    appetizer_cost = 8
    entree_cost = 20
    wine_cost = 3
    dessert_cost = 6
    discount = entree_cost / 2
    full_meal_cost = appetizer_cost + entree_cost + (2 * wine_cost) + dessert_cost
    actual_meal_cost = full_meal_cost - discount
    tip = full_meal_cost * 0.2
    total_cost = actual_meal_cost + tip
    return total_cost

print(solution())