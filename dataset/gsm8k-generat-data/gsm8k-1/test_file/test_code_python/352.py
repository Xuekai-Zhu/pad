def solution():
    """Dean's mother gave him $28 to go to the toy store. Dean bought 6 toy cars and 5 teddy bears. Each toy car cost $2 and each teddy bear cost $1. His mother then feels generous and decides to give him an extra $10. How much money does Dean have left?"""
    initial_money = 28
    num_cars = 6
    num_bears = 5
    car_cost = 2
    bear_cost = 1
    total_spent = num_cars * car_cost + num_bears * bear_cost
    total_money = initial_money + 10
    money_left = total_money - total_spent
    result = money_left
    return result

print(solution())