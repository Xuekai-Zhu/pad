def solution():
    # Calculate the time Laura spent at the park on one trip
    time_per_trip = 2 + 0.5  # 2 hours at the park plus 30 minutes walking

    # Calculate the total time Laura spent on all her trips
    total_time = 6 * time_per_trip

    # Calculate the time Laura spent at the park on all her trips
    time_at_park = 6 * 2

    # Calculate the percentage of time spent at the park
    percentage_at_park = (time_at_park / total_time) * 100
    result = percentage_at_park
    return result

print(solution())