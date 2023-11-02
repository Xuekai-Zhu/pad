def solution():
    """Frank goes to the store to buy some food. He buys 5 chocolate bars and 2 bags of chips.
    He hands the cashier $20 and gets $4 back as change. If the chocolate bars each cost $2, how much did each bag of chips cost?"""
    num_bars = 5
    bar_cost = 2
    total_bars_cost = num_bars * bar_cost
    money_paid = 20
    change_received = 4
    total_spent = money_paid - change_received
    chip_cost = (total_spent - total_bars_cost) / 2
    result = chip_cost
    return result

print(solution())