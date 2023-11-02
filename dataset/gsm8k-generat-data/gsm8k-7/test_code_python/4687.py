def solution():
    bus_time = "08:00"
    pick_up_time = "07:30"
    late_time = "07:50"

    # Convert time strings to datetime objects
    bus_time = datetime.datetime.strptime(bus_time, "%H:%M")
    pick_up_time = datetime.datetime.strptime(pick_up_time, "%H:%M")
    late_time = datetime.datetime.strptime(late_time, "%H:%M")

    # Calculate the time it takes for Delaney to reach the pick-up point
    travel_time = pick_up_time - late_time

    # Calculate the time difference between the bus time and the pick-up time
    time_difference = bus_time - pick_up_time

    # Calculate the total time Delaney missed the bus by
    missed_time = time_difference - travel_time
    result = missed_time
    return result

print(solution())