def solution():
    # Calculate the cost of the accessories
    computer_price = 3000
    accessories_price = 0.1 * computer_price

    # Calculate the amount of money Jeremy had before the purchase
    pre_purchase_money = 2 * computer_price

    # Calculate the total cost of the purchase
    total_cost = computer_price + accessories_price

    # Calculate the amount of money Jeremy has left after the purchase
    money_left = pre_purchase_money - total_cost
    
    result = money_left
    return result

print(solution())