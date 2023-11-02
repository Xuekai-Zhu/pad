def solution():
    jared_count = 300
    ann_count = jared_count / 0.85  # accounting for Jared counting 15% fewer cars than Ann
    alfred_count = ann_count - 7
    total_count = jared_count + ann_count + alfred_count
    result = total_count
    return result

print(solution())