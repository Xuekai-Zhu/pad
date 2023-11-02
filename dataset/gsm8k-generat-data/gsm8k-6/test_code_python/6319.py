def solution():
    # Calculate the total cost of 10 pairs of pants before the sale
    cost_before_sale = 10 * 45

    # Calculate the total cost of 10 pairs of pants after the 20% discount
    sale_discount = 0.20
    cost_after_sale = cost_before_sale - (sale_discount * cost_before_sale)

    # Calculate the total cost of 10 pairs of pants after the 10% tax
    tax_rate = 0.10
    total_cost = cost_after_sale + (tax_rate * cost_after_sale)

    result = total_cost
    return result

print(solution())