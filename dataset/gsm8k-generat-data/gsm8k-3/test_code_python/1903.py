def solution():
    """Allison, a YouTuber, uploads 10 one-hour videos of food reviews each day to her channel. She uploaded videos halfway through June, at that pace, and then doubled the number of video hours she uploaded on the remaining days. What's the total number of video hours she has uploaded at the end of the month?"""
    
    # Define the number of days in June
    days_in_june = 30
    
    # Calculate the number of video hours uploaded in the first half of June
    hours_in_first_half = 10 * (days_in_june // 2) # // is floor division

    # Calculate the number of video hours to be uploaded in the second half of June
    hours_in_second_half = 2 * hours_in_first_half

    # Calculate the total number of video hours uploaded for the entire month
    total_hours = hours_in_first_half + hours_in_second_half

    # Display the total number of video hours uploaded
    result = total_hours
    return result

print(solution())