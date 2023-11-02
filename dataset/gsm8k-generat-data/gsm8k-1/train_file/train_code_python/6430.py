def solution():
    """John decided to sell his PlayStation to buy a new computer. The computer's cost was $700 and the accessories cost was $200. The PlayStation was worth $400 but he sold it for 20% less than its value. How much money came out of his pocket?"""
    computer_cost = 700
    accessories_cost = 200
    ps_value = 400
    ps_sold_for = ps_value - (ps_value * 0.2)
    total_cost = computer_cost + accessories_cost + ps_sold_for
    money_out_of_pocket = total_cost
    return money_out_of_pocket

print(solution())