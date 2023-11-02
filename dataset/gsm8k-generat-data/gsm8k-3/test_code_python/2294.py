def solution():
    """There are three buckets full of oranges. There are 22 oranges in the first bucket, 17 more oranges in the second bucket and 11 fewer oranges in the third bucket than in the second. How many oranges are there in all the buckets?"""
    # Define the number of oranges in the first bucket
    oranges_1 = 22

    # Calculate the number of oranges in the second bucket
    oranges_2 = oranges_1 + 17

    # Calculate the number of oranges in the third bucket
    oranges_3 = oranges_2 - 11

    # Calculate the total number of oranges in all the buckets
    total_oranges = oranges_1 + oranges_2 + oranges_3

    # Display the total number of oranges
    result = total_oranges
    return result

print(solution())