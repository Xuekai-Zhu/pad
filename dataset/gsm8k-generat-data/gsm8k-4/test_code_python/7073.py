def solution():
    """Leila spent 3/4 of her savings on make-up and the rest on a sweater. If the sweater cost her $20, what were her original savings?"""
    # Define the cost of the sweater
    sweater_cost = 20

    # Determine how much money Leila spent on makeup
    makeup_spending = (3/4) * sweater_cost

    # Determine how much money Leila had left after buying the makeup
    remaining_money = sweater_cost - makeup_spending

    # Calculate Leila's original savings
    original_savings = remaining_money / (1/4)

    # return the result
    result = original_savings
    return result

print(solution())