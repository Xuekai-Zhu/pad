def solution():
    """Marcus is having a water balloon party. He has 100 balloons. Each balloon holds 3 ounces of water. He can buy 50 ounces of water for $2.5 a bottle. If he walks into the store with 2 $10 bills, how much change will he have after he buys all the water he needs?"""
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