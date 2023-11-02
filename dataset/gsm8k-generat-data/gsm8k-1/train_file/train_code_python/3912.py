def solution():
    """Marites internet speed is 10 megabits per second and her monthly internet bill is $20.
    Marites is planning to upgrade her service and choosing between 20 Mbps and 30 Mbps.
    If the price of the 30 Mbps is twice the amount of her current monthly bill and
    the price of the 20 Mbps is $10 more than her current monthly bill,
    how much will she save per year if she chooses the 20 Mbps than 30 Mbps?"""
    current_speed = 10
    current_bill = 20
    faster_speed = 30
    faster_price = current_bill * 2
    slower_speed = 20
    slower_price = current_bill + 10

    # Calculate annual cost for 30 Mbps plan
    annual_cost_faster = faster_price * 12

    # Calculate annual cost for 20 Mbps plan
    annual_cost_slower = slower_price * 12

    # Calculate annual savings if choosing 20 Mbps plan
    annual_savings = annual_cost_faster - annual_cost_slower
    result = annual_savings
    return result

print(solution())