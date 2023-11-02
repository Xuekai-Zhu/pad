def solution():
    prejean_speed_ratio = 0.75
    total_time = 70

    # Calculate the combined speed ratio of Prejean and Rickey
    combined_speed_ratio = 1 + prejean_speed_ratio

    # Calculate Rickey's speed ratio
    rickey_speed_ratio = combined_speed_ratio / 2

    # Calculate the time it took Rickey to finish the race
    rickey_time = total_time * (rickey_speed_ratio / combined_speed_ratio)

    result = rickey_time
    return result

print(solution())