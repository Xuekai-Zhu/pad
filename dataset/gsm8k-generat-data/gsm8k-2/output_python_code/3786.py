def solution():
    """Jason joined the military when he turned 18. It took him 8 years to raise to the rank of chief. Then 25% longer than that to go from chief to master chief. He then spent 10 years more in the military before retiring. How old was he when he retired?"""
    start_age = 18
    chief_time = 8
    master_chief_time = 1.25 * chief_time
    total_time = chief_time + master_chief_time + 10
    retired_age = start_age + total_time
    result = retired_age
    return result

print(solution())