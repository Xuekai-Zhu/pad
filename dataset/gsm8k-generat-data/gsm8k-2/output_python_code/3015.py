def solution():
    """Gary is buying chlorine for his rectangular pool, which is 10 feet long, 8 feet wide, and 6 feet deep. Gary needs to buy one quart of chlorine for every 120 cubic feet of water in his pool. If chlorine costs $3 a quart, how much does Gary spend on chlorine?"""
    length = 10
    width = 8
    depth = 6
    water_volume = length * width * depth
    chlorine_volume = water_volume / 120
    chlorine_cost = 3
    total_cost = chlorine_volume * chlorine_cost
    result = total_cost
    return result

print(solution())