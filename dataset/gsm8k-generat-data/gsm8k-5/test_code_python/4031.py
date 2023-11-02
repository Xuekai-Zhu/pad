def solution():
    total_strawberries = 300  # Cheryl placed 300 strawberries into 5 buckets
    buckets = 5  # Cheryl used 5 buckets
    strawberries_per_bucket = total_strawberries / buckets  # Calculate how many strawberries were originally in each bucket

    # Calculate how many strawberries are left in each bucket after taking out 20 from each bucket
    strawberries_left_per_bucket = strawberries_per_bucket - 20
    result = strawberries_left_per_bucket
    return result

print(solution())