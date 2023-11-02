def solution():
    """William is a jockey. He can ride his horse for 6 hours a day. Over 6 days, he only used the maximum riding time twice. On two days he rode his horse for only 1.5 hours a day and half the maximum time for the next two days. How many hours did William ride his horse during those 6 days?"""
    # Define the maximum riding time per day and the number of days
    MAX_RIDING_TIME = 6
    NUM_DAYS = 6

    # Define the number of days William rode his horse for the maximum riding time
    days_max_time = 2

    # Define the number of days William rode his horse for 1.5 hours
    days_1_5_time = 2

    # Define the number of days William rode his horse for half the maximum riding time
    days_half_time = 2

    # Calculate the total riding time for each type of day
    total_max_time = days_max_time * MAX_RIDING_TIME
    total_1_5_time = days_1_5_time * 1.5
    total_half_time = days_half_time * (MAX_RIDING_TIME / 2)

    # Calculate the total riding time for all six days
    total_riding_time = total_max_time + total_1_5_time + total_half_time

    # return the result
    result = total_riding_time
    return result

print(solution())