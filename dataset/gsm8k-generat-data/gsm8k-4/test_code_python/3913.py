def solution():
    """Marites internet speed is 10 megabits per second and her monthly internet bill is $20. Marites is planning to upgrade her service and choosing between 20 Mbps and 30 Mbps. If the price of the 30 Mbps is twice the amount of her current monthly bill and the price of the 20 Mbps is $10 more than her current monthly bill, how much will she save per year if she chooses the 20 Mbps than 30 Mbps?"""
    # Define the initial internet speed and bill
    initial_speed = 10
    initial_bill = 20

    # Define the price of the 20 Mbps and 30 Mbps options
    speed_20_price = initial_bill + 10
    speed_30_price = initial_bill * 2 

    # Calculate the annual cost of the 20 Mbps and 30 Mbps options
    annual_cost_20 = speed_20_price * 12
    annual_cost_30 = speed_30_price * 12

    # Calculate the savings of choosing the 20 Mbps option over the 30 Mbps option
    savings = annual_cost_30 - annual_cost_20

    result = savings
    return result

print(solution())