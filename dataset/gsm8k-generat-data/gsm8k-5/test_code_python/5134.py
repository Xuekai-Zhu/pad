def solution():
    jared_count = 300  # Jared counted 300 cars
    ann_count = jared_count / 0.85  # Jared counted 15% fewer cars than Ann
    alfred_count = ann_count - 7  # Ann counted 7 more cars than Alfred

    # Calculate the total number of cars counted by all three of them
    total_count = jared_count + ann_count + alfred_count
    result = total_count
    return result

print(solution())