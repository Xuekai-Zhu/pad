def solution():
    """Jared counted 15% fewer cars than his sister Ann while they were watching the road from the school, and Ann counted 7 more cars than their friend Alfred. If Jared counted 300 cars, how many cars did all of them count?"""
    # Define Jared's count
    jared_count = 300

    # Calculate Ann's count
    ann_count = jared_count / 0.85

    # Calculate Alfred's count
    alfred_count = ann_count - 7

    # Calculate the total count
    total_count = jared_count + ann_count + alfred_count

    result = round(total_count)
    return result

print(solution())