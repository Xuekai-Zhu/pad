def solution():
    """Marites internet speed is 10 megabits per second and her monthly internet bill is $20. Marites is planning to upgrade her service and choosing between 20 Mbps and 30 Mbps. If the price of the 30 Mbps is twice the amount of her current monthly bill and the price of the 20 Mbps is $10 more than her current monthly bill, how much will she save per year if she chooses the 20 Mbps than 30 Mbps?"""
    current_speed = 10
    current_bill = 20
    new_speed1 = 20
    new_bill1 = current_bill + 10
    new_speed2 = 30
    new_bill2 = current_bill * 2
    yearly_savings = (new_bill2 - new_bill1) * 12
    result = yearly_savings
    return result

print(solution())