def solution():
    """Mr. Langsley commutes to work every day by bus. The bus picks him up at 6:00 a.m. and takes forty minutes to arrive at the first station. If Mr. Langsley arrives at work at 9:00 a.m., what's the total time taken in minutes from the first station to Mr. Langsley's workplace?"""
    start_time = 6 * 60  # in minutes
    first_station_time = 40  # in minutes
    end_time = 9 * 60  # in minutes
    total_travel_time = end_time - (start_time + first_station_time)
    result = total_travel_time
    return result

print(solution())