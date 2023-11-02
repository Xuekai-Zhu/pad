def solution():
    total_money = 74
    sweater_price = 9
    tshirt_price = 11
    shoes_price = 30

    # Calculate the total amount spent
    total_spent = sweater_price + tshirt_price + shoes_price

    # Calculate the refund amount for the shoes
    shoes_refund = shoes_price * 0.9

    # Subtract the refund from the total spent
    total_spent -= shoes_refund

    # Calculate the money left
    money_left = total_money - total_spent
    result = money_left
    return result

print(solution())