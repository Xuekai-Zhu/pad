def solution():
    """A trader made a profit of $960 after a week of sales. To raise $610 to pay for her next shipment of wares, she splits the profit in half and solicits donations from her family and friends. If she received a total donation of $310 and adds it to one-half of her profit, how much money did she make above her goal?"""
    # Calculate the trader's half of the profit
    half_profit = 960 / 2

    # Calculate the total amount of money raised
    total_raised = half_profit + 310

    # Calculate the amount of money she made above her goal
    excess_money = total_raised - 610

    # Display the excess money made
    result = excess_money
    return result

print(solution())