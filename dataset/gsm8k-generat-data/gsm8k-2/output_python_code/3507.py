def solution():
    """Mr. Maxwell takes 1 hr to drive to work in the morning but 1 and half hours to drive back home in the evening. If the morning and evening traffic is similar and he drives at an average speed of 30mph in the morning, what is the average speed of his return journey?"""
    morning_distance = 30 * 1
    evening_distance = morning_distance
    evening_time = 1.5
    evening_speed = evening_distance / evening_time
    result = evening_speed
    return result

print(solution())