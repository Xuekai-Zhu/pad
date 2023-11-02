def solution():
    initial_money = 158
    shoe_cost = 45
    bag_cost = shoe_cost - 17
    lunch_cost = bag_cost / 4

    total_spent = shoe_cost + bag_cost + lunch_cost

    money_left = initial_money - total_spent
    result = money_left
    return result

print(solution())