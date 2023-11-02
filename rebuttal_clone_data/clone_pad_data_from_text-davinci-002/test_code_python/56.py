def solution():
    """Leo's assignment was divided into three parts. He finished the first part of his assignment in 25 minutes. It took him twice as long to finish the second part. If he was able to finish his assignment in 2 hours, how many minutes did Leo finish the third part of the assignment?"""
    first_part = 25
    second_part = first_part * 2
    total_time = first_part + second_part
    third_part = 120 - total_time
    result = third_part
    return result

print(solution())