def solution():
    """Buffy and Oz went to dinner. They shared an appetizer that cost $9.00. Each of their entrees was $20.00 and they shared a dessert that was $11.00. If they left a 30% tip, what was the entire price of the meal?"""
    # Define the prices of the appetizer, entrees, and dessert
    appetizer_price = 9
    entree_price = 20
    dessert_price = 11

    # Calculate the subtotal
    subtotal = appetizer_price + (2 * entree_price) + dessert_price

    # Calculate the tip
    tip_percentage = 0.3
    tip = subtotal * tip_percentage

    # Calculate the total price
    total_price = subtotal + tip

    result = total_price
    return result

print(solution())