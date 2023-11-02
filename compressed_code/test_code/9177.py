def solution():
    
    initial_money = 500
    potato_cost = 2
    tomato_cost = 3
    cucumber_cost = 4
    banana_cost = 5
    total_cost = (6 * potato_cost) + (9 * tomato_cost) + (5 * cucumber_cost) + (3 * banana_cost)
    remaining_money = initial_money - total_cost
    result = remaining_money
    return result

print(solution())