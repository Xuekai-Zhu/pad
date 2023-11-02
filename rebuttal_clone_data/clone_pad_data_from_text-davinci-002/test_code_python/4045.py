def solution():
    trips_to_park = 6
    time_spent_at_park = 2
    time_spent_walking = 0.5
    total_time_spent = trips_to_park * (time_spent_at_park + time_spent_walking)
    time_spent_in_park = trips_to_park * time_spent_at_park
    percentage = time_spent_in_park / total_time_spent
    result = percentage
    return result

print(solution())