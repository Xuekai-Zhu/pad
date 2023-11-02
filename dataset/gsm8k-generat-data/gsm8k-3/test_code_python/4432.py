def solution():
    """Shane wants to take as many photos as possible this year. He takes 146 photos in the first 2 months of the year. In January, he takes 2 photos every day. The rest of the photos were taken in February. If in February he took an equal number of photos each week, how many photos did Shane take each week in February?"""
    # Define the number of days in January and February
    JANUARY_DAYS = 31
    FEBRUARY_DAYS = 28

    # Calculate the total number of photos taken in January
    january_photos = 2 * JANUARY_DAYS

    # Calculate the number of photos taken in February
    february_photos = 146 - january_photos

    # Calculate the number of photos taken each week in February
    weekly_photos = february_photos / 4

    # Display the number of photos taken each week in February
    result = weekly_photos
    return result

print(solution())