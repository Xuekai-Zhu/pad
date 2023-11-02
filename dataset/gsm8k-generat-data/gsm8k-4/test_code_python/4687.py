def solution():
    """Delaney has to catch a bus that leaves at 8:00. a.m to school every day. He always takes 30 minutes to reach the pick-up point from his home. One day he woke up late and left his home at 7:50. How much time did he miss the bus by when he reached the pick-up point?"""
    # Define the time it takes Delaney to reach the pick-up point
    time_to_reach_pickup_point = 30

    # Define the time the bus leaves
    bus_leaving_time = "8:00 a.m"

    # Define the time Delaney left his home on the day he woke up late
    delaney_leaving_time = "7:50 a.m"

    # Calculate the time difference between Delaney leaving his home and the bus leaving
    time_difference = (pd.to_datetime(bus_leaving_time) - pd.to_datetime(delaney_leaving_time)).total_seconds() / 60

    # Subtract the time it takes Delaney to reach the pick-up point
    time_missed = time_difference - time_to_reach_pickup_point

    # Return the time Delaney missed the bus by
    result = time_missed
    return result

print(solution())