def solution():
    """The water pressure of a sink has a steady flow of 2 cups per 10 minutes for the first 30 minutes. It still flows at 2 cups per 10 minutes for the next 30 minutes after. For the next hour, the water pressure maximizes to 4 cups per 10 minutes and stops. Shawn now has to dump half of the water away. How much water is left?"""
    steady_flow_rate = 2/10 # cups per minute
    first_hour = steady_flow_rate * 60 # cups in the first hour
    double_flow_rate = 4/10 # cups per minute
    second_hour = double_flow_rate * 60 # cups in the second hour
    total_water = first_hour + second_hour # total cups of water
    half_water = total_water / 2 # half of total water in cups
    result = half_water
    return result

print(solution())