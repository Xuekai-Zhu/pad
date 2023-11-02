def solution():
    """John started weightlifting when he was 16. When he first started he could Clean & Jerk 80 kg and he could Snatch 50 kg. He manages to double his clean and jerk and increase his snatch by 80%. What is his new combined total lifting capacity?"""
    initial_cj = 80
    initial_snatch = 50
    new_cj = initial_cj * 2
    snatch_increase = initial_snatch * 0.8
    new_snatch = initial_snatch + snatch_increase
    total_capacity = new_cj + new_snatch
    result = total_capacity
    return result

print(solution())