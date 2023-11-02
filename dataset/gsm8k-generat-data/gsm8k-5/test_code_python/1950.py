def solution():
    total_cost = 20 - 4  # Frank pays $20 and gets $4 back, so the total cost is $16
    chocolate_bars = 5  # Frank buys 5 chocolate bars at $2 each, which is $10 in total
    chocolate_cost = 10
    bags_of_chips = 2  # Frank buys 2 bags of chips
    chips_cost = (total_cost - chocolate_cost) / bags_of_chips  # The cost of the chips is the remaining balance after paying for the chocolate bars
    result = chips_cost
    return result

print(solution())