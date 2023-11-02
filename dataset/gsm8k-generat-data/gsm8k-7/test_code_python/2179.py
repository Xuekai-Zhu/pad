def solution():
    first_podcast = 0.75  # 45 minutes = 0.75 hours
    second_podcast = 1.5 * first_podcast  # twice as long
    third_podcast = 1.75  # 1 hour and 45 minutes = 1.75 hours
    fourth_podcast = 1.0  # 1 hour

    # Calculate the total length of the first four podcasts
    total_length = first_podcast + second_podcast + third_podcast + fourth_podcast

    # Calculate how much time is left in the 6-hour drive
    time_left = 6 - total_length

    result = time_left
    return result

print(solution())