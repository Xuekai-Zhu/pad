def solution():
    
    eden_buckets = 4
    mary_buckets = eden_buckets + 3
    iris_buckets = mary_buckets - 1
    total_buckets = eden_buckets + mary_buckets + iris_buckets
    sand_weight_per_bucket = 2
    total_sand_weight = total_buckets * sand_weight_per_bucket
    result = total_sand_weight
    return result

print(solution())