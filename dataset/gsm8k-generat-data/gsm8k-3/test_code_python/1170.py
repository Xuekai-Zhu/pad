def solution():
    """Andy is running late. School starts at 8:00 AM and it normally takes him 30 minutes to get there, but today he had to stop for 3 minutes each at 4 red lights and wait 10 minutes to get past construction. If he left his house at 7:15, how many minutes late will he be?"""
    # Calculate the total time it takes Andy to get to school today
    normal_time = 30
    red_lights_time = 3 * 4
    construction_time = 10
    total_time = normal_time + red_lights_time + construction_time

    # Calculate the time he leaves his house
    departure_time = 7*60 + 15

    # Calculate the time he arrives at school
    arrival_time = departure_time + total_time

    # Calculate how late he will be
    tardiness = arrival_time - 8*60

    # Display how many minutes late he will be
    result = tardiness
    return result

print(solution())