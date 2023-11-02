def solution():
    num_strawberries = 300
    num_buckets = 5
    strawberries_per_bucket = num_strawberries / num_buckets
    strawberries_left_per_bucket = strawberries_per_bucket - 20
    result = strawberries_left_per_bucket
    return result

print(solution())