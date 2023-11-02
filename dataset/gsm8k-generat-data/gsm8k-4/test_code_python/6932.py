def solution():
    """Diana gets 30 minutes of video game time for every hour she reads. Her dad decided to raise her reward by 20%. Diana read for 12 hours this week. How many more minutes of video game time will she get as a result of her raise?"""
    # Define the initial video game time and the increase percentage
    initial_vgt_time = 0
    increase_percentage = 0.2

    # Define the number of hours read by Diana
    hours_read = 12

    # Calculate the initial video game time earned by Diana
    initial_vgt_time = hours_read * 30

    # Calculate the increased video game time earned by Diana
    increased_vgt_time = initial_vgt_time * increase_percentage

    # Calculate the total video game time earned by Diana
    total_vgt_time = initial_vgt_time + increased_vgt_time

    # Calculate the difference in video game time earned between the initial and increased amounts
    difference_vgt_time = increased_vgt_time

    # return the result
    result = difference_vgt_time
    return result

print(solution())