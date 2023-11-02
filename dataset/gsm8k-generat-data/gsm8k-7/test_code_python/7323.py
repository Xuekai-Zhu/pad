def solution():
    check_in_time = 2  # hours
    driving_time = 0.75  # hours (45 minutes)
    parking_time = 0.25  # hours (15 minutes)
    flight_time = 20  # hours (8:00 pm + 20 hours)

    # Calculate the total amount of time needed for check-in and travel
    total_time = check_in_time + driving_time + parking_time

    # Subtract the total time from the flight time to determine the latest departure time
    latest_departure_time = flight_time - total_time
    result = "{:.0f}:{:02.0f} pm".format(latest_departure_time, (latest_departure_time % 1) * 60)
    return result

print(solution())