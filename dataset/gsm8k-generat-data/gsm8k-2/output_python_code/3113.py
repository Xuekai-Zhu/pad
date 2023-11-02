def solution():
    """Jill sells girl scout cookies. This year, she wants to sell at least 150 cookie boxes. Her first customer buys 5 boxes, Her second one buys 4 times more than her first customer. Her third customer buys half as much as her second. The fourth customer buys 3 times as much as her third. Lastly, her final customer buys 10. How many boxes so Jill have left to sell to hit her sales goal?"""
    sales_goal = 150
    first_customer = 5
    second_customer = 4 * first_customer
    third_customer = 0.5 * second_customer
    fourth_customer = 3 * third_customer
    final_customer = 10
    total_sold = first_customer + second_customer + third_customer + fourth_customer + final_customer
    boxes_left = sales_goal - total_sold
    result = boxes_left
    return result

print(solution())