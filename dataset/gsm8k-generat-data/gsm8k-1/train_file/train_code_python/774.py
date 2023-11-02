def solution():
    """Three buckets are holding different fruits. Bucket A has 4 more pieces of fruit than bucket B while bucket B has 3 more pieces of fruit than bucket C. If bucket C has 9 pieces of fruit, how many pieces of fruit are in all 3 buckets?"""
    bucket_c = 9
    bucket_b = bucket_c + 3
    bucket_a = bucket_b + 4
    total_fruit = bucket_a + bucket_b + bucket_c
    result = total_fruit
    return result

print(solution())