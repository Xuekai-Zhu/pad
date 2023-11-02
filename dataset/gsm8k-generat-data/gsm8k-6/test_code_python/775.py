def solution():
    # Find the number of fruits in bucket B and A
    fruits_in_bucketC = 9
    fruits_in_bucketB = fruits_in_bucketC + 3
    fruits_in_bucketA = fruits_in_bucketB + 4

    # Find the total number of fruits in all 3 buckets
    total_fruits = fruits_in_bucketC + fruits_in_bucketB + fruits_in_bucketA
    result = total_fruits
    return result

print(solution())