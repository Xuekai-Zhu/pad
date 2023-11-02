def solution():
    lee_money = 10
    friend_money = 8
    wings_cost = 6
    salad_cost = 4
    soda_cost = 2
    tax = 3
    total_cost = wings_cost + salad_cost + soda_cost + tax
    total_money = lee_money + friend_money
    change = total_money - total_cost
    result = change
    return result

print(solution())