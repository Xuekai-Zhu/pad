def solution():
    # Convert arrival time in Cape Town to hours elapsed since departure
    cape_town_arrival = 34  # 10am ET on Tuesday is 2pm SAST on Tuesday
    elapsed_time = cape_town_arrival - 6  # Convert to hours elapsed since departure

    # Subtract flight time from London to New York to get flight time from New York to Cape Town
    flight_time_ny_to_ct = elapsed_time - 18
    result = flight_time_ny_to_ct
    return result

print(solution())