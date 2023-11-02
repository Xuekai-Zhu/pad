def solution():
    """Three buckets are holding different fruits. Bucket A has 4 more pieces of fruit than bucket B while bucket B has 3 more pieces of fruit than bucket C. If bucket C has 9 pieces of fruit, how many pieces of fruit are in all 3 buckets?"""
    # Define the number of fruits in bucket C
    fruits_c = 9

    # Calculate the number of fruits in bucket B
    fruits_b = fruits_c + 3

    # Calculate the number of fruits in bucket A
    fruits_a = fruits_b + 4

    # Calculate the total number of fruits in all three buckets
    total_fruits = fruits_a + fruits_b + fruits_c

    # return the result
    result = total_fruits
    return result

print(solution())