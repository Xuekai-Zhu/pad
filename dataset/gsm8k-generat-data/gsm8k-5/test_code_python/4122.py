def solution():
    total_pictures = 960  # Alex has 960 pictures to process
    time_per_picture = 2  # It will take 2 minutes to process each picture

    # Calculate the total time it will take to process all the pictures
    total_time = (total_pictures * time_per_picture) / 60  # Convert minutes to hours

    result = total_time
    return result

print(solution())