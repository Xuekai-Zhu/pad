def solution():
    
    total_strawberries = 300
    num_buckets = 5
    strawberries_per_bucket = total_strawberries // num_buckets
    strawberries_left = strawberries_per_bucket - 20
    result = strawberries_left
    return result

print(solution())