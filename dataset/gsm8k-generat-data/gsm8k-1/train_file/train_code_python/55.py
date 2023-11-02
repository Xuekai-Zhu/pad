def solution():
    """Leo's assignment was divided into three parts. He finished the first part of his assignment in 25 minutes. It took him twice as long to finish the second part. If he was able to finish his assignment in 2 hours, how many minutes did Leo finish the third part of the assignment?"""
    total_time = 2 * 60  # convert 2 hours to minutes
    first_part_time = 25
    second_part_time = 2 * first_part_time  # twice as long as the first part
    third_part_time = total_time - (first_part_time + second_part_time)
    result = third_part_time
    return result

print(solution())