def solution():
    """There are three buckets full of oranges. There are 22 oranges in the first bucket, 17 more oranges in the second bucket and 11 fewer oranges in the third bucket than in the second. How many oranges are there in all the buckets?"""
    # Define the number of oranges in the first bucket
    oranges_first = 22

    # Calculate the number of oranges in the second bucket
    oranges_second = oranges_first + 17

    # Calculate the number of oranges in the third bucket
    oranges_third = oranges_second - 11

    # Calculate the total number of oranges in all buckets
    total_oranges = oranges_first + oranges_second + oranges_third

    # return the result
    result = total_oranges
    return result

print(solution())