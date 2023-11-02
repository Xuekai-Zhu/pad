def solution():
    oil_cost = 13
    oil_amount = 2
    pasta_cost = 4
    pasta_amount = 3
    sauce_cost = 5
    sauce_amount = 1
    total_cost = (oil_cost * oil_amount) + (pasta_cost * pasta_amount) + (sauce_cost * sauce_amount)
    remaining_money = 50 - total_cost
    result = "${:.2f}".format(remaining_money)
    return result

print(solution())