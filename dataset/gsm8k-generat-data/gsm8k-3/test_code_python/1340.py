def solution():
    """William is a jockey. He can ride his horse for 6 hours a day. Over 6 days, he only used the maximum riding time twice.  On two days he rode his horse for only 1.5 hours a day and half the maximum time for the next two days. How many hours did William ride his horse during those 6 days?"""
    # Define the maximum time William can ride his horse per day
    MAX_RIDING_TIME = 6

    # Calculate the total riding time for the 6 days
    riding_time = 0
    # William used the maximum riding time twice
    riding_time += MAX_RIDING_TIME * 2
    # William rode his horse for 1.5 hours on two days
    riding_time += 1.5 * 2
    # William rode his horse for half the maximum time on two days
    riding_time += (MAX_RIDING_TIME / 2) * 2

    # Display the total riding time
    result = riding_time
    return result

print(solution())