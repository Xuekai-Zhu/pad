def solution():
    computer_cost = 700
    accessories_cost = 200
    playstation_value = 400
    playstation_sale_percent = 20

    # Calculate the selling price of the PlayStation after the discount
    playstation_sale_price = playstation_value - (playstation_value * (playstation_sale_percent / 100))

    # Calculate the total amount of money John spent
    total_spent = computer_cost + accessories_cost - playstation_sale_price
    result = total_spent
    return result

print(solution())