def solution():
    first_bucket_oranges = 22
    second_bucket_oranges = first_bucket_oranges + 17
    third_bucket_oranges = second_bucket_oranges - 11

    # Calculate the total number of oranges in all three buckets
    total_oranges = first_bucket_oranges + second_bucket_oranges + third_bucket_oranges
    result = total_oranges
    return result

print(solution())