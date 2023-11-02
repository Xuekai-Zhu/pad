def solution():
    num_planes = 5
    rows_per_plane = 20
    seats_per_row = 7
    num_flights_per_plane = 2

    # Calculate the total number of seats per plane
    seats_per_plane = rows_per_plane * seats_per_row

    # Calculate the total number of passengers per plane per day
    passengers_per_plane_per_day = seats_per_plane * num_flights_per_plane

    # Calculate the total number of passengers per day for all planes
    total_passengers_per_day = passengers_per_plane_per_day * num_planes
    result = total_passengers_per_day
    return result

print(solution())