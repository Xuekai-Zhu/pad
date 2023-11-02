def solution():
    original_budget = 60  # Yvette's original budget was $60
    extra_cost = 0.2 * original_budget  # The frame Yvette wanted is 20% more expensive than her budget
    new_price = original_budget + extra_cost  # The new price of the frame Yvette wanted
    smaller_price = 0.75 * new_price  # Yvette paid for a smaller frame at 3/4 the new price of the frame she initially wanted

    # Calculate how much money Yvette remained with
    remaining_money = original_budget - smaller_price
    result = remaining_money
    return result

print(solution())