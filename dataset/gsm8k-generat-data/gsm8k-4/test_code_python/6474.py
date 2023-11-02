def solution():
    """Two companies A and B, are selling bottled milk. Company A sells a big bottle for $4 and Company B sells a big bottle for $3.5. Company A was able to sell 300 and company B 350 big bottles of milk. How much more money did one company make from the other?"""
    # Define the prices and quantities sold by each company
    price_a = 4
    quantity_a = 300
    price_b = 3.5
    quantity_b = 350

    # Calculate the total sales revenue for each company
    revenue_a = price_a * quantity_a
    revenue_b = price_b * quantity_b

    # Determine which company made more revenue
    if revenue_a > revenue_b:
        difference = revenue_a - revenue_b
        result = difference
    else:
        difference = revenue_b - revenue_a
        result = difference
    return result

print(solution())