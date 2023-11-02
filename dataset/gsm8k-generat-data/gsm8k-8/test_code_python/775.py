def solution():
    # Define the number of fruit in bucket C
    bucket_c = 9

    # Calculate the number of fruit in bucket B
    bucket_b = bucket_c + 3

    # Calculate the number of fruit in bucket A
    bucket_a = bucket_b + 4

    # Calculate the total number of fruit in all three buckets
    total_fruit = bucket_a + bucket_b + bucket_c
    result = total_fruit
    return result

print(solution())