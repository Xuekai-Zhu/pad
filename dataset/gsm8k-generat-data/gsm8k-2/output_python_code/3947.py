def solution():
    """John started weightlifting when he was 16. When he first started he could Clean & Jerk 80 kg and he could Snatch 50 kg. He manages to double his clean and jerk and increase his snatch by 80%. What is his new combined total lifting capacity?"""
    clean_and_jerk = 80 * 2
    snatch = 50 * 1.8
    total_capacity = clean_and_jerk + snatch
    result = total_capacity
    return result

print(solution())