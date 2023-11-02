def solution():
    num_trips_per_day = 4
    capacity_per_trip = 12
    num_days = 2

    # Calculate the total capacity of the boat in one day
    total_capacity_per_day = num_trips_per_day * capacity_per_trip

    # Calculate the total capacity of the boat in two days
    total_capacity_per_two_days = total_capacity_per_day * num_days
    result = total_capacity_per_two_days
    return result

print(solution())