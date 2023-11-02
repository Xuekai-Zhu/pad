def solution():
    # Calculate the time of arrival in New York relative to London time
    arrival_time_NY = 6 + 18  # 18 hours later than 6:00 a.m. ET on Monday is 12:00 p.m. ET

    # Calculate the time of departure from New York relative to London time
    departure_time_NY = arrival_time_NY + 5  # The time difference between London and New York is 5 hours

    # Calculate the time of arrival in Cape Town relative to London time
    arrival_time_CT = departure_time_NY + 15  # The time difference between New York and Cape Town is 15 hours

    # Calculate the duration of the flight from New York to Cape Town
    duration = (arrival_time_CT - departure_time_NY) % 24  # Account for crossing the International Date Line

    result = duration
    return result

print(solution())