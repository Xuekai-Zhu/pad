def solution():
    """Mr. Langsley commutes to work every day by bus. The bus picks him up at 6:00 a.m. and takes forty minutes to arrive at the first station. If Mr. Langsley arrives at work at 9:00 a.m.,
    what's the total time taken in minutes from the first station to Mr. Langsley's workplace?"""
    # Define the time the bus picks up Mr. Langsley
    pickup_time = 6*60 # 6:00 a.m. in minutes

    # Define the time the bus arrives at the first station
    station_time = pickup_time + 40

    # Define the time Mr. Langsley arrives at work
    work_time = 9*60 # 9:00 a.m. in minutes

    # Calculate the total time taken from the first station to Mr. Langsley's workplace
    total_time = work_time - station_time

    # Display the total time in minutes
    result = total_time
    return result

print(solution())