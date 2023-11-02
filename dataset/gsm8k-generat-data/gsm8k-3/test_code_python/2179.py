def solution():
    """Roger had a 6-hour drive planned out.  He didn't want to listen to music so he downloaded several podcasts.  The first podcast was 45 minutes long.  The second podcast was twice as long as that.  The third podcast was 1 hour and 45 minutes long.  His fourth podcast is 1 hour long.  How many hours will his next podcast have to be to fill up the full 6 hours?"""
    # Calculate the total length of the first 4 podcasts
    total_podcast_length = (45/60) + (2*45/60) + (105/60) + 1

    # Calculate the remaining time for the drive
    remaining_time = 6 - total_podcast_length

    # Calculate the required length for the next podcast
    required_length = remaining_time

    # Convert the required length to minutes and round to the nearest 5 minutes
    required_length_minutes = round(required_length * 60 / 5) * 5

    # Convert the required length back to hours and round to 1 decimal place
    required_length_hours = round(required_length_minutes / 60, 1)

    # Display the required length for the next podcast
    result = required_length_hours
    return result

print(solution())