def solution():
    """Kiki likes to spend her money on hats and scarves. When she buys twice as many hats as scarves, she spends 60% of her money on hats and the rest on scarves. If she currently has $90, how many scarves will she buy if they are sold at $2 each?"""
    # Define the price of each scarf
    scarf_price = 2

    # Calculate Kiki's total spending on hats
    hat_spending_percentage = 60
    hat_spending = 0.6 * 90

    # Calculate Kiki's total spending on scarves
    total_spending = 90
    scarf_spending = total_spending - hat_spending
    scarf_quantity = scarf_spending / scarf_price

    # Calculate the number of hats Kiki bought
    hat_quantity = 2 * scarf_quantity

    # Calculate the number of scarves Kiki will buy next
    next_scarf_quantity = hat_quantity / 2

    result = next_scarf_quantity
    return result

print(solution())