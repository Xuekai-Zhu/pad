def solution():
    """Carson is refilling his tires. Each tire can hold 500 cubic inches of air. Two of the tires are completely flat and empty. One tire is 40% full and the last tire is 70% full. If Carson injects 50 cubic inches of air with each pump, how many pumps will it take him to fill all the tires?"""
    tire_capacity = 500
    empty_tires = 2
    tire_40_percent = tire_capacity * 0.4
    tire_70_percent = tire_capacity * 0.7
    total_air_needed = (2 * tire_capacity) - tire_40_percent - tire_70_percent
    pumps_needed = total_air_needed / 50
    result = pumps_needed
    return result

print(solution())