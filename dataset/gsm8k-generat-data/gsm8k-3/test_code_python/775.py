def solution():
    """Three buckets are holding different fruits. Bucket A has 4 more pieces of fruit than bucket B while bucket B has 3 more pieces of fruit than bucket C. If bucket C has 9 pieces of fruit, how many pieces of fruit are in all 3 buckets?"""
    # Define the number of pieces of fruit in bucket C
    c = 9

    # Calculate the number of pieces of fruit in bucket B
    b = c + 3

    # Calculate the number of pieces of fruit in bucket A
    a = b + 4

    # Calculate the total number of pieces of fruit in all 3 buckets
    total_fruit = a + b + c

    # Display the total number of pieces of fruit
    result = total_fruit
    return result

print(solution())