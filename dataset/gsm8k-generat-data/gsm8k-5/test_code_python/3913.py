def solution():
    current_speed = 10  # Marites' current internet speed is 10 Mbps
    current_bill = 20  # Marites' current monthly internet bill is $20

    # Prices for upgraded internet speeds
    price_20Mbps = current_bill + 10  # $10 more than the current bill
    price_30Mbps = current_bill * 2  # Twice the amount of the current bill

    # Calculate the difference in cost for a year between 30 Mbps and 20 Mbps
    yearly_cost_30Mbps = price_30Mbps * 12  # Total cost for a year with 30 Mbps
    yearly_cost_20Mbps = price_20Mbps * 12  # Total cost for a year with 20 Mbps
    cost_difference = yearly_cost_30Mbps - yearly_cost_20Mbps

    result = cost_difference
    return result

print(solution())