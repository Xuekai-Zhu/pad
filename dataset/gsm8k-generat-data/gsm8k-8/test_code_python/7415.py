def solution():
    total_time = 38
    downstairs_time = (total_time - 5) / (2 + 1)  # 2+1 represents the ratio of upstairs_time to downstairs_time
    upstairs_time = downstairs_time * 2 + 5
    result = upstairs_time
    return result

print(solution())