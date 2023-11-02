def solution():
    """It takes John 13 seconds to run 100 meters. He only goes 4 meters in the first second. He then maintains the same speed for the rest of the race. James is 2 m/s faster at the top speed and he can run the first 10 meters in 2 seconds. How long does it take James to run 100 meters?"""
    john_speed = 100 / 13
    john_acceleration = (john_speed - 4) / 1
    john_time_to_reach_max_speed = (john_speed - 4) / john_acceleration
    john_constant_speed_distance = 100 - 4 - (john_speed * john_time_to_reach_max_speed - 0.5 * john_acceleration * john_time_to_reach_max_speed ** 2)
    
    james_speed = john_speed + 2
    james_acceleration = (james_speed - 10 / 2) / 2
    james_time_to_reach_max_speed = (james_speed - 10 / 2) / james_acceleration
    james_constant_speed_distance = 100 - 10 - (james_speed * james_time_to_reach_max_speed - 0.5 * james_acceleration * james_time_to_reach_max_speed ** 2)
    
    james_time = james_time_to_reach_max_speed + james_constant_speed_distance / james_speed
    result = james_time
    return result

print(solution())