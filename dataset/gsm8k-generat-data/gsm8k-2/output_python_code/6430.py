def solution():
    """John decided to sell his PlayStation to buy a new computer. The computer's cost was $700 and the accessories cost was $200. The PlayStation was worth $400 but he sold it for 20% less than its value. How much money came out of his pocket?"""
    computer_cost = 700
    accessories_cost = 200
    playstation_value = 400
    playstation_sale_price = playstation_value - (0.2 * playstation_value)
    total_cost = computer_cost + accessories_cost + (playstation_sale_price)
    money_out_of_pocket = total_cost - playstation_value
    result = money_out_of_pocket
    return result

print(solution())