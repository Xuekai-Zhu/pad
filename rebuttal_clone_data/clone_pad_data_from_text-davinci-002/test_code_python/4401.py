def solution():
    adidas = 45
    nike = 60
    reebok = 35
    adidas_shoes = 8
    nike_shoes = 6
    reebok_shoes = 9
    total_cost = (adidas * adidas_shoes) + (nike * nike_shoes) + (reebok * reebok_shoes)
    goal = 1000
    result = total_cost - goal
    return result

print(solution())