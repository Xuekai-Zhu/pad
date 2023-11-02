def solution():
    """Chance boarded a plane departing from London to New York at 6:00 a.m. ET on Monday. He arrived in New York 18 hours later. If he took another plane flying to Cape town the day he arrived in New York and arrived in Cape town at 10:00 a.m ET on Tuesday, calculate the number of hours his flight took from New York to cape town."""
    # Define the time difference between New York and Cape town
    time_difference = 6

    # Calculate the time of arrival in New York
    arrival_time_ny = datetime.datetime(2022, 10, 17, 6, 0, 0)

    # Calculate the time of departure from New York to Cape town
    departure_time_ny = datetime.datetime(2022, 10, 18, 10, 0, 0)

    # Calculate the time difference between arrival in New York and departure to Cape town
    time_difference_ny_ct = (departure_time_ny - arrival_time_ny).total_seconds() / 3600

    result = time_difference_ny_ct
    return result

print(solution())