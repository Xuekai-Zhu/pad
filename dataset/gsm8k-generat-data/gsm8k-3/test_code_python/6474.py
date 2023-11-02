def solution():
    """Two companies A and B, are selling bottled milk. Company A sells a big bottle for $4 and Company B sells a big bottle for $3.5. Company A was able to sell 300 and company B 350 big bottles of milk. How much more money did one company make from the other?"""
    # Define the price and quantity of milk for each company
    COMPANY_A_PRICE = 4
    COMPANY_B_PRICE = 3.5
    COMPANY_A_QUANTITY = 300
    COMPANY_B_QUANTITY = 350

    # Calculate the total revenue for each company
    company_a_revenue = COMPANY_A_PRICE * COMPANY_A_QUANTITY
    company_b_revenue = COMPANY_B_PRICE * COMPANY_B_QUANTITY

    # Calculate the difference in revenue between the two companies
    revenue_difference = abs(company_a_revenue - company_b_revenue)

    # Determine which company made more revenue and by how much
    if company_a_revenue > company_b_revenue:
        result = f"Company A made ${revenue_difference} more than Company B."
    elif company_b_revenue > company_a_revenue:
        result = f"Company B made ${revenue_difference} more than Company A."
    else:
        result = "Both companies made the same amount of revenue."

    return result

print(solution())