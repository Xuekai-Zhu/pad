def solution():
    """Leila spent 3/4 of her savings on make-up and the rest on a sweater. If the sweater cost her $20, what were her original savings?"""
    # Define the cost of the sweater
    SWEATER_COST = 20

    # Calculate the fraction of Leila's savings spent on make-up
    makeup_fraction = 3/4

    # Calculate the fraction of Leila's savings remaining after buying the sweater
    remaining_fraction = 1 - makeup_fraction

    # Calculate the cost of the make-up
    makeup_cost = remaining_fraction * SWEATER_COST / makeup_fraction

    # Calculate Leila's original savings
    original_savings = makeup_cost + SWEATER_COST

    # Display Leila's original savings
    result = original_savings
    return result

print(solution())