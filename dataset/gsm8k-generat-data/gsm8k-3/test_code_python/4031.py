def solution():
    """Cheryl placed 300 strawberries into 5 buckets. After she did that she decided to take 20 out of each bucket so they wouldn't get smashed. How many strawberries were left in each bucket?"""
    # Define the number of strawberries and buckets
    NUM_STRAWBERRIES = 300
    NUM_BUCKETS = 5

    # Calculate the number of strawberries in each bucket before removing some
    strawberries_per_bucket = NUM_STRAWBERRIES / NUM_BUCKETS

    # Calculate the number of strawberries in each bucket after removing 20 from each
    strawberries_per_bucket -= 20

    # Display the number of strawberries in each bucket
    result = strawberries_per_bucket
    return result

print(solution())