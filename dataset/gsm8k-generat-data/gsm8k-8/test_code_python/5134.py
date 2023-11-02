def solution():
    # Define Jared's count
    jared_count = 300

    # Calculate Ann's count (15% more than Jared's count)
    ann_count = jared_count / (1 - 0.15)

    # Calculate Alfred's count (7 less than Ann's count)
    alfred_count = ann_count - 7

    # Calculate the total count
    total_count = jared_count + ann_count + alfred_count
    result = total_count
    return result

print(solution())