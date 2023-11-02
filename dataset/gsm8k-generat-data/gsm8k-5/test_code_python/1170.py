def solution():
    normal_travel_time = 30  # It normally takes Andy 30 minutes to get to school
    red_light_stops = 4  # Andy has to stop for 3 minutes at 4 red lights
    construction_wait_time = 10  # Andy has to wait 10 minutes to get past construction
    total_extra_time = (red_light_stops * 3) + construction_wait_time  # Calculate the total extra time Andy spent

    # Calculate the total travel time for Andy today
    total_travel_time = normal_travel_time + total_extra_time

    # Calculate how many minutes late Andy will be
    departure_time = 7 * 60 + 15  # Convert departure time to minutes
    arrival_time = departure_time + total_travel_time  # Calculate arrival time in minutes
    late_time = arrival_time - 8 * 60  # Calculate how many minutes late Andy will be
    result = late_time
    return result

print(solution())