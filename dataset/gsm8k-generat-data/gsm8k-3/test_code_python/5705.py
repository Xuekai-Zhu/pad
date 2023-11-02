def solution():
    """Kiki likes to spend her money on hats and scarves. When she buys twice as many hats as scarves, she spends 60% of her money on hats and the rest on scarves. If she currently has $90, how many scarves will she buy if they are sold at $2 each?"""
    # Define the cost of a scarf
    SCARF_PRICE = 2

    # Calculate Kiki's total spending on hats
    hat_spending_percentage = 60
    total_spending = 90
    hat_spending = total_spending * (hat_spending_percentage / 100)

    # Calculate the number of hats and scarves Kiki bought
    hat_to_scarf_ratio = 2
    hat_count = hat_spending / hat_to_scarf_ratio
    scarf_count = hat_count / hat_to_scarf_ratio

    # Calculate Kiki's spending on scarves
    scarf_spending = total_spending - hat_spending
    scarf_cost = scarf_count * SCARF_PRICE

    # Calculate the number of scarves Kiki will buy
    result = scarf_count
    return result

print(solution())