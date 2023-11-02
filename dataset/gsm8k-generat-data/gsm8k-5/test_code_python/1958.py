def solution():
    prejean_speed_ratio = 0.75  # Prejean's speed is 3/4 of Rickey's speed
    total_race_time = 70  # They both took a total of 70 minutes to run the race
    rickey_time_ratio = 1 / (1 + prejean_speed_ratio)  # Calculate the ratio of Rickey's time to the total race time

    # Calculate Rickey's time in minutes
    rickey_time = rickey_time_ratio * total_race_time

    result = rickey_time
    return result

print(solution())