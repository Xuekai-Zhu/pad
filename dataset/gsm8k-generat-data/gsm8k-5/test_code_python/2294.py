def solution():
    # Find the number of oranges in the second bucket
    oranges_second_bucket = 22 + 17

    # Find the number of oranges in the third bucket
    oranges_third_bucket = oranges_second_bucket - 11

    # Find the total number of oranges in all three buckets
    total_oranges = 22 + oranges_second_bucket + oranges_third_bucket
    result = total_oranges
    return result

print(solution())