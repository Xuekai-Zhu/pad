def solution():
    """Andy is running late. School starts at 8:00 AM and it normally takes him 30 minutes to get there, but today he had to stop for 3 minutes each at 4 red lights and wait 10 minutes to get past construction. If he left his house at 7:15, how many minutes late will he be?"""
    # Define the time it takes to get to school without delays
    normal_time = 30

    # Define the time spent waiting at red lights
    red_light_time = 3 * 4

    # Define the time spent waiting for construction
    construction_time = 10

    # Calculate the total delay time
    delay_time = red_light_time + construction_time

    # Calculate the actual time it will take him to get to school today
    actual_time = normal_time + delay_time

    # Define the time he left his house
    leave_time = 7 * 60 + 15

    # Define the time school starts
    school_time = 8 * 60

    # Calculate how many minutes late he will be
    late_time = actual_time + leave_time - school_time

    # Return the result
    result = late_time
    return result

print(solution())