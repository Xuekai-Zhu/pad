def solution():
    money_total = 158
    shoes_cost = 45
    bag_cost = 17
    lunch_cost = bag_cost / 4
    money_left = money_total - shoes_cost - bag_cost - lunch_cost
    result = money_left
    return result

print(solution())