def solution():
    """Mr. Maxwell takes 1 hr to drive to work in the morning but 1 and half hours to drive back home in the evening. If the morning and evening traffic is similar and he drives at an average speed of 30mph in the morning, what is the average speed of his return journey?"""
    morning_time = 1
    evening_time = 1.5
    morning_speed = 30
    return_speed = (2 * morning_speed * morning_time) / evening_time
    result = return_speed
    return result

print(solution())