def solution():
    # Define the number of strawberries and buckets
    num_strawberries = 300
    num_buckets = 5

    # Calculate the number of strawberries in each bucket before removal
    strawberries_per_bucket = num_strawberries / num_buckets

    # Calculate the number of strawberries in each bucket after removal
    strawberries_remaining = strawberries_per_bucket - 20

    result = strawberries_remaining
    return result

print(solution())