def solution():
    """Allison, a YouTuber, uploads 10 one-hour videos of food reviews each day to her channel. She uploaded videos halfway through June, at that pace, and then doubled the number of video hours she uploaded on the remaining days. What's the total number of video hours she has uploaded at the end of the month?"""
    # Define the number of days in June
    JUNE_DAYS = 30

    # Calculate the number of videos uploaded per day for the first half of June
    videos_per_day_first_half = 10

    # Calculate the total number of hours of videos uploaded in the first half of June
    total_hours_first_half = videos_per_day_first_half * JUNE_DAYS * 0.5

    # Calculate the number of videos uploaded per day for the second half of June
    videos_per_day_second_half = videos_per_day_first_half * 2

    # Calculate the total number of hours of videos uploaded in the second half of June
    total_hours_second_half = videos_per_day_second_half * JUNE_DAYS * 0.5

    # Calculate the total number of hours of videos uploaded in June
    total_hours_june = total_hours_first_half + total_hours_second_half

    # return the result
    result = total_hours_june
    return result

print(solution())