def solution():
    """There are 3 numbers that are consecutive integers. Together they have a sum of 18. What is the largest of the 3 numbers?"""
    total_sum = 18
    middle_num = total_sum // 3
    largest_num = middle_num + 2
    result = largest_num
    return result

print(solution())