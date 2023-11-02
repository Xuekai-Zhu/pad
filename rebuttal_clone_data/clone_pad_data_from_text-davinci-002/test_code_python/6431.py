def solution():
    computer_cost = 700
    accessories_cost = 200
    playstation_value = 400
    playstation_sale_price = playstation_value - (playstation_value * 0.2)
    total_cost = computer_cost + accessories_cost + playstation_sale_price
    result = total_cost
    
    return result

print(solution())