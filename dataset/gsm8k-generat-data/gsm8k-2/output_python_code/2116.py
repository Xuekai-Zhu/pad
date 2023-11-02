def solution():
    """Two friends are racing three miles. The first one runs it in 21 minutes. The second one runs it in 24 minutes. If they keep up the same pace, how long combined will it take for them to run 5 miles each?"""
    dist = 5
    friend1_time = (dist / 3) * 21
    friend2_time = (dist / 3) * 24
    total_time = friend1_time + friend2_time
    result = total_time
    return result

print(solution())