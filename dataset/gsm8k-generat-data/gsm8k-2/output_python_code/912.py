def solution():
    """A trader made a profit of $960 after a week of sales. To raise $610 to pay for her next shipment of wares, she splits the profit in half and solicits donations from her family and friends. If she received a total donation of $310 and adds it to one-half of her profit, how much money did she make above her goal?"""
    total_profit = 960
    goal_amount = 610
    remaining_profit = total_profit - (goal_amount / 2)
    total_donations = 310
    total_amount_raised = remaining_profit + total_donations
    amount_above_goal = total_amount_raised - goal_amount
    result = amount_above_goal
    return result

print(solution())