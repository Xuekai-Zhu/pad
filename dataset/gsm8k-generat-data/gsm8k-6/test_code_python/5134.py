def solution():
    jared_count = 300 # Jared counted 300 cars
    ann_count = jared_count / 0.85 # Ann counted 15% more cars than Jared
    alfred_count = ann_count - 7 # Alfred counted 7 fewer cars than Ann
    total_count = jared_count + ann_count + alfred_count # Add up all the car counts
    result = total_count
    return result

print(solution())