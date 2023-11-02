def solution():
    start_time = 6*60  # Mr. Langsley starts his commute at 6:00 a.m. in minutes
    first_station_arrival = start_time + 40  # The bus takes 40 minutes to arrive at the first station
    work_arrival = 9*60  # Mr. Langsley arrives at work at 9:00 a.m. in minutes

    # Calculate the total time taken in minutes from the first station to Mr. Langsley's workplace
    total_time = work_arrival - first_station_arrival
    result = total_time
    return result

print(solution())