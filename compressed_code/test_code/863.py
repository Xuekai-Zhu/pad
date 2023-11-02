def solution():
    
    balloons = 100
    water_per_balloon = 3
    total_water = balloons * water_per_balloon
    water_per_bottle = 50
    cost_per_bottle = 2.5
    total_bottles = total_water / water_per_bottle
    total_cost = total_bottles * cost_per_bottle
    payment = 10 * 2
    change = payment - total_cost
    result = change
    return result

print(solution())