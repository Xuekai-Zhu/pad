def solution():
    """The news announced a $0.4 oil price rollback this Friday. Mr. Deane decided to only fill his gas tank with 10 liters of gas today and then another 25 liters on Friday. If the cost per liter of gas is $1.4 today, how much will Mr. Deane spend for his 35 liters of gas?"""
    cost_per_liter = 1.4
    friday_price = cost_per_liter - 0.4
    first_purchase = 10 * cost_per_liter
    second_purchase = 25 * friday_price
    total_cost = first_purchase + second_purchase
    result = total_cost
    return result

print(solution())