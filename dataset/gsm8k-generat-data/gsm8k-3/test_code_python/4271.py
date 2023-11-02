def solution():
    """It takes 15 minutes for Dante to go to Hidden Lake. From Hidden Lake, he has to walk back to the Park Office and it takes him 7 minutes. When he arrives there, he will have been gone from the Park Office 32 minutes altogether. If he had walked to the Lake Park restaurant from the Park office before taking the 15 minute walk to Hidden Lake, how long is the walk from Park Office to the Lake Park restaurant?"""
    # Define the time it takes Dante to get to Hidden Lake
    hidden_lake_time = 15

    # Define the time it takes Dante to walk back to the Park Office from Hidden Lake
    back_to_park_office_time = 7

    # Define the total time Dante was gone from the Park Office
    total_time = 32

    # Calculate the time it took Dante to walk from the Park Office to Hidden Lake
    park_office_to_hidden_lake_time = total_time - hidden_lake_time - back_to_park_office_time

    # Calculate the time it took Dante to walk from the Park Office to the Lake Park restaurant
    park_office_to_restaurant_time = park_office_to_hidden_lake_time - hidden_lake_time

    # Display the time it takes to walk from the Park Office to the Lake Park restaurant
    result = park_office_to_restaurant_time
    return result

print(solution())