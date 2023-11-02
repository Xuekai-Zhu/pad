def solution():
    # Calculate the total cost of the order
    total_cost = 2*15 + 6*3 + 6*2  # 2 quiches at $15 each, 6 croissants at $3 each, 6 buttermilk biscuits at $2 each
    # Check if the total order is over $50 to apply the 10% discount
    if total_cost > 50:
        total_cost *= 0.9  # apply the 10% discount
    result = total_cost
    return result

print(solution())