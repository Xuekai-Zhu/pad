def solution():
    departure_time = 8 * 60  # The bus leaves at 8:00 a.m., converted to minutes
    travel_time = 30  # It takes Delaney 30 minutes to reach the pick-up point
    late_start_time = 7 * 60 + 50  # Delaney left his home at 7:50 a.m., converted to minutes

    # Calculate the time Delaney arrives at the pick-up point
    arrival_time = late_start_time + travel_time

    # Calculate how many minutes late Delaney was for the bus
    minutes_late = departure_time - arrival_time
    result = minutes_late
    return result

print(solution())