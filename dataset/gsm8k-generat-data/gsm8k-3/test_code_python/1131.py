def solution():
    """Tire repair for each tire costs $7, plus another 50 cents for sales tax. If Juan needs all 4 tires repaired, how much is the final cost?"""
    # Define the cost per tire and the sales tax amount
    COST_PER_TIRE = 7
    SALES_TAX = 0.5

    # Calculate the total cost for all 4 tires
    total_cost = (COST_PER_TIRE + SALES_TAX) * 4

    # Display the final cost
    result = total_cost
    return result

print(solution())