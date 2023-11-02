def solution():
    """Eden, Mary and Iris gather sand to fill their sandbox. Eden carried 4 buckets of sand. Mary carried 3 more buckets of sand than Eden. Iris carried 1 less bucket of sand than Mary. If each bucket contains 2 pounds of sand, how many pounds of sand did they collect in total?"""
    eden_buckets = 4
    mary_buckets = eden_buckets + 3
    iris_buckets = mary_buckets - 1
    total_buckets = eden_buckets + mary_buckets + iris_buckets
    pounds_per_bucket = 2
    total_pounds = total_buckets * pounds_per_bucket
    result = total_pounds
    
    return result

print(solution())