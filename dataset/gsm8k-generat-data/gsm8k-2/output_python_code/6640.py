def solution():
    """A giant spider is discovered. It weighs 2.5 times the previous largest spider, which weighed 6.4 ounces. Each of its legs has a cross-sectional area of .5 square inches. How much pressure in ounces per square inch does each leg undergo?"""
    previous_weight = 6.4
    giant_weight = 2.5 * previous_weight
    leg_area = 0.5
    pressure = giant_weight / (8 * leg_area)  # spiders have 8 legs
    result = pressure
    return result

print(solution())