def solution():
    num_flights = 3
    up_and_down_per_trip = num_flights * 2
    num_trips_up = 5
    num_trips_down = 3

    # Calculate the total flights of stairs walked up and down
    total_up_and_down = up_and_down_per_trip * (num_trips_up + num_trips_down)

    result = total_up_and_down
    return result

print(solution())