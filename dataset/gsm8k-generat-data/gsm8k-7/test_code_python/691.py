def solution():
    london_to_ny_time = 18  # in hours
    ny_to_cape_town_time = 28  # in hours

    # Calculate the time of arrival in New York in ET time
    arrival_time_ny_et = (6 + london_to_ny_time) % 24

    # Calculate the time difference between New York and Cape Town in hours
    time_diff_ny_cape_town = 6

    # Calculate the time of arrival in Cape Town in New York time
    arrival_time_cape_town_ny_time = (10 - time_diff_ny_cape_town) % 24

    # Calculate the total time from New York to Cape Town in hours
    total_time = (24 - arrival_time_ny_et) + arrival_time_cape_town_ny_time + ny_to_cape_town_time
    result = total_time
    return result

print(solution())