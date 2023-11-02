def solution():
    """It takes John 13 seconds to run 100 meters.  He only goes 4 meters in the first second.  He then maintains the same speed for the rest of the race.  James is 2 m/s faster at the top speed and he can run the first 10 meters in 2 seconds.  How long does it take James to run 100 meters?"""
    # Define John's speed and time for the last 12 seconds of the race
    john_speed = 96/12 # John runs 96 meters in 12 seconds
    john_time = 12

    # Define James's speed and time for the last 90 meters of the race
    james_speed = john_speed + 2 # James's top speed is 2 m/s faster than John's
    james_time = 90/james_speed

    # Add up the times for the first and last parts of the race for James
    total_time = james_time + 2

    # Display James's total time to run 100 meters
    result = total_time
    return result

print(solution())