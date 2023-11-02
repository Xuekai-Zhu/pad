def solution():
    """Jared counted 15% fewer cars than his sister Ann while they were watching the road from the school, and Ann counted 7 more cars than their friend Alfred. If Jared counted 300 cars, how many cars did all of them count?"""
    jared_count = 300
    ann_count = jared_count * (100 / 85)
    alfred_count = ann_count - 7
    total_count = jared_count + ann_count + alfred_count
    result = total_count
    return result

print(solution())