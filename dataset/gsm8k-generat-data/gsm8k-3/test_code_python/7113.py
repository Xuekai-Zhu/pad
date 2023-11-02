def solution():
    """Darius has 5 buckets of water. One contains 11 ounces, one contains 13 ounces, one contains 12 ounces,
    one contains 16 ounces, and one contains 10 ounces. He pours the ten-ounce bucket into a bigger bucket,
    along with one of the other four. The total in the bigger bucket is now 23 ounces. He pours the remaining
    three buckets into a second large bucket. How many ounces does the second large bucket contain?"""
    # Define the given bucket sizes
    bucket_sizes = [11, 13, 12, 16, 10]
    # Define the total amount in the bigger bucket after pouring the 10-ounce bucket
    bigger_bucket_total = 23
    # Determine which two buckets were used to fill the bigger bucket
    for i in range(len(bucket_sizes)):
        for j in range(i + 1, len(bucket_sizes)):
            if bucket_sizes[i] + bucket_sizes[j] == bigger_bucket_total - 10:
                # The remaining three buckets are the ones not used to fill the bigger bucket
                remaining_buckets = bucket_sizes[:i] + bucket_sizes[i+1:j] + bucket_sizes[j+1:]
                # Calculate the total amount in the second large bucket
                second_bucket_total = sum(remaining_buckets)
                # Display the total amount in the second large bucket
                result = second_bucket_total
                return result

print(solution())