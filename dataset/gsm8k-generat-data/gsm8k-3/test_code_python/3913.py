def solution():
    """Marites internet speed is 10 megabits per second and her monthly internet bill is $20. Marites is planning to upgrade her service and choosing between 20 Mbps and 30 Mbps. If the price of the 30 Mbps is twice the amount of her current monthly bill and the price of the 20 Mbps is $10 more than her current monthly bill, how much will she save per year if she chooses the 20 Mbps than 30 Mbps?"""
    # Define Marites' current internet speed and monthly bill
    CURRENT_SPEED = 10
    CURRENT_BILL = 20

    # Define the prices for the 20 and 30 Mbps plans
    PLAN_20_PRICE = CURRENT_BILL + 10
    PLAN_30_PRICE = CURRENT_BILL * 2

    # Calculate the annual cost for each plan
    PLAN_20_COST = PLAN_20_PRICE * 12
    PLAN_30_COST = PLAN_30_PRICE * 12

    # Calculate the annual savings if Marites chooses the 20 Mbps plan instead of the 30 Mbps plan
    ANNUAL_SAVINGS = PLAN_30_COST - PLAN_20_COST

    # Display the annual savings
    result = ANNUAL_SAVINGS
    return result

print(solution())