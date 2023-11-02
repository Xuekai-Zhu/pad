def solution():
    """Leo's assignment was divided into three parts. He finished the first part of his assignment in 25 minutes.
    It took him twice as long to finish the second part. If he was able to finish his assignment in 2 hours, 
    how many minutes did Leo finish the third part of the assignment?"""
    
    # Define the total time spent on the assignment in minutes
    total_time = 120

    # Define the time spent on the first part of the assignment
    part1_time = 25

    # Define the time spent on the second part of the assignment
    part2_time = 2 * part1_time

    # Calculate the time spent on the third part of the assignment
    part3_time = total_time - part1_time - part2_time

    result = part3_time
    return result

print(solution())