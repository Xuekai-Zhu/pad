def solution():
    """Shane wants to take as many photos as possible this year. He takes 146 photos in the first 2 months of the year. In January, he takes 2 photos every day. The rest of the photos were taken in February. If in February he took an equal number of photos each week, how many photos did Shane take each week in February?"""
    # Define the total number of photos taken in the first 2 months
    total_photos = 146

    # Calculate the number of photos taken in January
    january_photos = 2 * 31

    # Calculate the number of photos taken in February
    february_photos = total_photos - january_photos

    # Calculate the number of weeks in February
    weeks_in_february = 4

    # Calculate the number of photos taken each week in February
    weekly_photos_february = february_photos / weeks_in_february

    # return the result
    result = weekly_photos_february
    return result

print(solution())