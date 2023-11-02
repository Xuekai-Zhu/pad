def solution():
    total_money = 74  # Will's mom gave him $74 to go shopping
    sweater_cost = 9
    tshirt_cost = 11
    shoes_cost = 30

    # Calculate the total cost of the items Will bought
    total_cost = sweater_cost + tshirt_cost + shoes_cost

    # Calculate the refund amount for the shoes
    shoes_refund = shoes_cost * 0.9

    # Calculate the total amount spent and refunded
    net_spent = total_cost - shoes_refund

    # Calculate the money Will has left
    money_left = total_money - net_spent
    result = money_left
    return result

print(solution())