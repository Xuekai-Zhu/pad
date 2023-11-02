def solution():
    num_trips = 6
    park_time = 2.0
    walking_time = 0.5

    # Calculate the total time Laura spent on all her trips
    total_time = (park_time + walking_time) * num_trips

    # Calculate the total time Laura spent in the park
    total_park_time = park_time * num_trips

    # Calculate the percentage of time Laura spent in the park
    percentage_in_park = (total_park_time / total_time) * 100
    result = percentage_in_park
    return result

print(solution())