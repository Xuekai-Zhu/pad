def solution():
    """It takes John 13 seconds to run 100 meters. He only goes 4 meters in the first second. He then maintains the same speed for the rest of the race. James is 2 m/s faster at the top speed and he can run the first 10 meters in 2 seconds. How long does it take James to run 100 meters?"""
    john_speed = 100 / 13   # meters per second
    john_first_sec = 4   # meters
    john_rest_of_race = 100 - john_first_sec   # meters
    john_rest_of_race_time = john_rest_of_race / john_speed   # seconds

    james_top_speed = john_speed + 2   # meters per second
    james_first_10_meters_time = 2   # seconds
    james_rest_of_race = 100 - 10   # meters
    james_rest_of_race_time = james_rest_of_race / james_top_speed   # seconds

    total_time = james_first_10_meters_time + james_rest_of_race_time
    result = total_time
    return result

print(solution())