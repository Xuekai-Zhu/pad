def solution():
    """Every 10 seconds, there is a car collision, and every 20 seconds there is a big crash. How many accidents overall will happen in 4 minutes?"""
    car_collision_rate = 6  # once every 10 seconds is 6 times per minute
    big_crash_rate = 3  # once every 20 seconds is 3 times per minute
    total_time = 4 * 60  # 4 minutes in seconds
    car_collision_count = car_collision_rate * total_time // 60  # using floor division to round down to nearest whole number
    big_crash_count = big_crash_rate * total_time // 60
    total_accidents = car_collision_count + big_crash_count
    result = total_accidents
    return result

print(solution())