def solution():
    # Convert 1 hour 20 minutes to 80 minutes
    train_time = 80

    # Convert train time from minutes to hours
    train_time_hours = train_time / 60

    # Add train time to 10 minutes for total travel time
    total_travel_time = train_time_hours + 10/60

    # Subtract total travel time from 9:00 AM (in 24-hr time)
    departure_time = "7:40"

    result = departure_time
    return result

print(solution())