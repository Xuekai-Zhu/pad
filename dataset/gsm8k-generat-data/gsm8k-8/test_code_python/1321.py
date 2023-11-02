def solution():
    # Define the total cost of the items before tax
    total_cost_before_tax = 150

    # Calculate the amount of sales tax
    sales_tax = 0.08 * total_cost_before_tax

    # Calculate the total cost of the items with sales tax
    total_cost_with_tax = total_cost_before_tax + sales_tax
    result = total_cost_with_tax
    return result

print(solution())