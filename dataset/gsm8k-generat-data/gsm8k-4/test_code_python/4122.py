def solution():
    """Alex has taken pictures of all of the plants in a park near her home. She wants to find out how many of each plant she has pictures of.
    She has 960 pictures, and counting them all will take her a long time. It will take the program 2 minutes to process each picture. How many hours will it take to process all of the pictures?"""
    # Define the number of pictures and the time to process each picture
    num_pictures = 960
    time_per_picture = 2  # in minutes

    # Calculate the total time required to process all pictures
    total_time_minutes = num_pictures * time_per_picture
    total_time_hours = total_time_minutes / 60

    # Round up the total time to the nearest hour
    total_time_hours = round(total_time_hours + 0.5)

    result = total_time_hours
    return result

print(solution())