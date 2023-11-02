def solution():
    # Calculate the total number of oranges in all buckets
    total_oranges = 22 + (22 + 17) + (22 + 17 - 11)  # 22 oranges in the first bucket, 17 more oranges in the second bucket, 11 fewer in the third
    result = total_oranges
    return result

print(solution())