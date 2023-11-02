def solution():
    """The water pressure of a sink has a steady flow of 2 cups per 10 minutes for the first 30 minutes. It still flows at 2 cups per 10 minutes for the next 30 minutes after. For the next hour, the water pressure maximizes to 4 cups per 10 minutes and stops. Shawn now has to dump half of the water away. How much water is left?"""
    steady_flow = 2
    steady_time = 60
    steady_water = steady_flow * (30 + 30)
    max_flow = 4
    max_time = 60
    max_water = max_flow * max_time
    total_water = steady_water + max_water
    half_water = total_water / 2
    result = total_water - half_water
    return result

print(solution())