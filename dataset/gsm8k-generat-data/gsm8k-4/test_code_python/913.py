def solution():
    """A trader made a profit of $960 after a week of sales. To raise $610 to pay for her next shipment of wares, she splits the profit in half and solicits donations from her family and friends. If she received a total donation of $310 and adds it to one-half of her profit, how much money did she make above her goal?"""
    # Define the profit and the amount needed for the next shipment
    profit = 960
    shipment_cost = 610

    # Calculate the amount of profit needed to reach the shipment cost
    target_profit = shipment_cost + (profit/2)

    # Calculate the total amount of money received from family and friends
    donations = 310

    # Calculate the total amount of money made above the goal
    above_goal = (profit/2) + donations - target_profit

    result = above_goal
    return result

print(solution())