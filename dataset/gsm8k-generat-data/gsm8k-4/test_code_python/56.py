def solution():
    """Leo's assignment was divided into three parts. He finished the first part of his assignment in 25 minutes. It took him twice as long to finish the second part. If he was able to finish his assignment in 2 hours, how many minutes did Leo finish the third part of the assignment?"""
    # Define the total time it took to complete the assignment
    total_time = 120  # 2 hours in minutes

    # Define the time it took to complete the first part
    first_part_time = 25

    # Define the time it took to complete the second part (twice the time of the first part)
    second_part_time = 2 * first_part_time

    # Calculate the time it took to complete the third part
    third_part_time = total_time - first_part_time - second_part_time

    # return the result
    result = third_part_time
    return result

print(solution())