def solution():
    """Cheryl placed 300 strawberries into 5 buckets. After she did that she decided to take 20 out of each bucket so they wouldn't get smashed. How many strawberries were left in each bucket?"""
    total_strawberries = 300
    num_buckets = 5
    strawberries_per_bucket = total_strawberries / num_buckets
    strawberries_left = strawberries_per_bucket - 20
    result = strawberries_left
    return result

print(solution())