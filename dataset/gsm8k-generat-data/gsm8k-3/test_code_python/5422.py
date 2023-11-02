def solution():
    """There are 3 numbers that are consecutive integers. Together they have a sum of 18. What is the largest of the 3 numbers?"""
    # Define the sum of the three numbers
    sum_ = 18

    # Find the middle number by dividing the sum by 3 and rounding down
    middle_num = sum_ // 3

    # Find the largest number by adding 1 to the middle number
    largest_num = middle_num + 1

    # Display the largest number
    result = largest_num
    return result

print(solution())