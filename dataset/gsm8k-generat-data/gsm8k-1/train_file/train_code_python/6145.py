def solution():
    """Erika and her brother Rick want to buy a gift for their mother that costs $250. They have both saved money. Erika saved $155 and her brother saved only half of the cost of the gift. They also want to surprise their mother with a birthday cake that costs $25. How much money will they have left after buying their mother a gift and cake?"""
    cost_of_gift = 250
    erika_savings = 155
    rick_savings = cost_of_gift / 2
    total_money = erika_savings + rick_savings
    money_left = total_money - (cost_of_gift + 25)
    result = money_left
    return result

print(solution())