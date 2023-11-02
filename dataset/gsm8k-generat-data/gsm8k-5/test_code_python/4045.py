def solution():
    num_trips = 6
    time_per_trip = 2.5  # 2 hours in the park + 30 minutes walking
    total_time = num_trips * time_per_trip

    # Calculate the total time spent in the park
    time_in_park = num_trips * 2  # 2 hours per trip

    # Calculate the percentage of total time spent in the park
    percentage_in_park = (time_in_park / total_time) * 100
    result = percentage_in_park
    return result

print(solution())