def solution():
    """John buys 1000 balloons. Each balloon holds 10 liters of air. If he buys 500-liter tanks of gas, how many tanks does he need to buy to fill all the balloons?"""
    balloons = 1000
    liters_per_balloon = 10
    liters_per_tank = 500
    total_liters = balloons * liters_per_balloon
    tanks_needed = total_liters // liters_per_tank + 1
    result = tanks_needed
    
    return result

print(solution())