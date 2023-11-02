def solution():
    """Roger had a 6-hour drive planned out. He didn't want to listen to music so he downloaded several podcasts. The first podcast was 45 minutes long. The second podcast was twice as long as that. The third podcast was 1 hour and 45 minutes long. His fourth podcast is 1 hour long. How many hours will his next podcast have to be to fill up the full 6 hours?"""
    # Define the length of the first four podcasts in minutes
    podcast1_length = 45
    podcast2_length = 2 * podcast1_length
    podcast3_length = 105
    podcast4_length = 60

    # Calculate the total length of the first four podcasts in minutes
    total_length = podcast1_length + podcast2_length + podcast3_length + podcast4_length

    # Convert the total length to hours
    total_length_hours = total_length / 60

    # Calculate the remaining time for the 6-hour drive
    remaining_time_hours = 6 - total_length_hours

    result = remaining_time_hours
    return result

print(solution())