def solution():
    profit = 960  # The trader made a profit of $960
    donation_goal = 610  # The trader needs to raise $610 for her next shipment

    # Split the profit in half
    half_profit = profit / 2

    # Calculate the amount of additional donations the trader needs
    needed_donations = donation_goal - half_profit

    # Calculate the total amount of donations received
    total_donations = 310

    # Calculate the total amount of money made above the goal
    money_above_goal = (half_profit + total_donations) - donation_goal
    result = money_above_goal
    return result

print(solution())