def solution():
    # Calculate the cost of 3 liters of chlorine
    original_cost_chlorine = 10 * 3  # $10 per liter, 3 liters
    discount_chlorine = 0.20  # 20% discount
    discounted_cost_chlorine = original_cost_chlorine - (original_cost_chlorine * discount_chlorine)

    # Calculate the cost of 5 boxes of soap
    original_cost_soap = 16 * 5  # $16 per box, 5 boxes
    discount_soap = 0.25  # 25% discount
    discounted_cost_soap = original_cost_soap - (original_cost_soap * discount_soap)

    # Calculate the total amount saved
    total_savings = (original_cost_chlorine - discounted_cost_chlorine) + (original_cost_soap - discounted_cost_soap)
    result = total_savings
    return result

print(solution())