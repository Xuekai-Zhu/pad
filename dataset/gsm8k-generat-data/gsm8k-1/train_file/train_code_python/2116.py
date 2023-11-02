def solution():
    """Two friends are racing three miles. The first one runs it in 21 minutes. The second one runs it in 24 minutes. If they keep up the same pace, how long combined will it take for them to run 5 miles each?"""
    first_runner_time = 21
    second_runner_time = 24
    total_distance = 5
    combined_time = (total_distance / 3) * (first_runner_time + second_runner_time)
    result = combined_time
    return result

print(solution())