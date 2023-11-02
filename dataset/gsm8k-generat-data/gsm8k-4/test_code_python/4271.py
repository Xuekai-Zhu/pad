def solution():
    """It takes 15 minutes for Dante to go to Hidden Lake. From Hidden Lake, he has to walk back to the Park Office and it takes him 7 minutes. When he arrives there, he will have been gone from the Park Office 32 minutes altogether. If he had walked to the Lake Park restaurant from the Park office before taking the 15 minute walk to Hidden Lake, how long is the walk from Park Office to the Lake Park restaurant?"""
    # Define the time it takes for Dante to walk from Hidden Lake to the Park Office
    lake_to_office_time = 7

    # Define the total time Dante was gone from the Park Office
    total_time_away = 32

    # Define the time it takes for Dante to walk to Hidden Lake
    lake_time = 15

    # Calculate the time Dante spent at the Hidden Lake
    lake_time_spent = total_time_away - lake_to_office_time - lake_time

    # Calculate the time Dante spent walking to the Lake Park restaurant before going to Hidden Lake
    restaurant_time = total_time_away - lake_to_office_time - lake_time - lake_time_spent

    # return the result
    result = restaurant_time
    return result

print(solution())