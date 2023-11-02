def solution():
    """A giant spider is discovered. It weighs 2.5 times the previous largest spider, which weighed 6.4 ounces. Each of its legs has a cross-sectional area of .5 square inches. How much pressure in ounces per square inch does each leg undergo?"""
    previous_spider_weight = 6.4
    giant_spider_weight = previous_spider_weight * 2.5
    leg_area = 0.5
    total_legs = 8
    total_pressure = giant_spider_weight / (total_legs * leg_area)
    result = total_pressure
    return result

print(solution())