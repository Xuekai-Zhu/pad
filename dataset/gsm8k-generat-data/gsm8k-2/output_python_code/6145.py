def solution():
    """Erika and her brother Rick want to buy a gift for their mother that costs $250. They have both saved money. Erika saved $155 and her brother saved only half of the cost of the gift. They also want to surprise their mother with a birthday cake that costs $25. How much money will they have left after buying their mother a gift and cake?"""
    gift_cost = 250
    erika_money = 155
    rick_money = gift_cost / 2
    total_money = erika_money + rick_money
    cake_cost = 25
    remaining_money = total_money - gift_cost - cake_cost
    result = remaining_money
    return result

print(solution())