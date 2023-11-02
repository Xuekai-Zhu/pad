def solution():
    """Cho hiked 14 kilometers per hour for 8 hours. Chloe hiked 9 kilometers per hour and stopped after 5 hours. How many kilometers farther did Cho hike?"""
    cho_speed = 14
    cho_time = 8
    cho_distance = cho_speed * cho_time
    chloe_speed = 9
    chloe_time = 5
    chloe_distance = chloe_speed * chloe_time
    distance_difference = cho_distance - chloe_distance
    result = distance_difference
    return result

print(solution())