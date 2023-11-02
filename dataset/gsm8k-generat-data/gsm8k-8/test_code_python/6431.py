def solution():
    # Calculate the price John sold his PlayStation for
    ps_value = 400
    ps_sale_percent = 20
    ps_sale_amount = ps_value * ps_sale_percent / 100
    ps_sale_price = ps_value - ps_sale_amount

    # Calculate the total cost of the computer and accessories
    computer_cost = 700
    accessories_cost = 200
    total_cost = computer_cost + accessories_cost

    # Calculate the total money John spent
    money_spent = total_cost - ps_sale_price

    result = money_spent
    return result

print(solution())