def solution():
    """Leo's assignment was divided into three parts. He finished the first part of his assignment in 25 minutes. It took him twice as long to finish the second part. If he was able to finish his assignment in 2 hours, how many minutes did Leo finish the third part of the assignment?"""
    total_time = 120
    part1_time = 25
    part2_time = 2*part1_time
    part3_time = total_time - part1_time - part2_time
    result = part3_time
    return result

print(solution())