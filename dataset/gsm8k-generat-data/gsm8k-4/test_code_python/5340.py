def solution():
    """It takes John 13 seconds to run 100 meters. He only goes 4 meters in the first second.
    He then maintains the same speed for the rest of the race. James is 2 m/s faster at the top
    speed and he can run the first 10 meters in 2 seconds. How long does it take James to run 100 meters?"""
    # Define the distance and time data for John's run
    john_distance = 100
    john_first_second = 4
    john_total_time = 13

    # Calculate John's average speed (excluding the first second)
    john_speed = (john_distance - john_first_second) / (john_total_time - 1)

    # Define the distance and time data for James's run
    james_distance = 100
    james_first_10m = 10
    james_first_2s = 2
    james_top_speed = john_speed + 2

    # Calculate the time it takes James to run the first 10 meters at his initial speed
    james_initial_time = james_first_2s

    # Calculate the time it takes James to run the remaining 90 meters at his top speed
    james_top_speed_distance = james_distance - james_first_10m
    james_top_speed_time = james_top_speed_distance / james_top_speed

    # Calculate James's total running time
    james_total_time = james_initial_time + james_top_speed_time

    result = james_total_time
    return result

print(solution())