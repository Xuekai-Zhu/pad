def solution():
    """Cheryl placed 300 strawberries into 5 buckets. After she did that she decided to take 20 out of each bucket so they wouldn't get smashed. How many strawberries were left in each bucket?"""
    # Define the initial number of strawberries and buckets
    initial_strawberries = 300
    num_buckets = 5

    # Determine the number of strawberries in each bucket before removing 20
    strawberries_per_bucket = initial_strawberries / num_buckets

    # Determine the number of strawberries in each bucket after removing 20
    final_strawberries_per_bucket = strawberries_per_bucket - 20

    result = final_strawberries_per_bucket
    return result

print(solution())