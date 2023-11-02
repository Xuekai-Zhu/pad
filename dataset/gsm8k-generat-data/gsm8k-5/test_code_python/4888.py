def solution():
    bicycle_cost = 150  # The bicycle costs $150
    amount_saved = bicycle_cost / 2  # Patrick saved half the price of the bicycle
    amount_lent = 50  # Patrick lent $50 to his friend

    # Calculate how much money Patrick has now
    current_amount = amount_saved - amount_lent
    result = current_amount
    return result

print(solution())