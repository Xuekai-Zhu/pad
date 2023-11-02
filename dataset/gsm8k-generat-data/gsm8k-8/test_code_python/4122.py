def solution():
    # Define the number of pictures and the processing time per picture
    num_pictures = 960
    time_per_picture = 2  # in minutes

    # Calculate the total processing time in minutes and convert to hours
    total_processing_time = num_pictures * time_per_picture
    hours = total_processing_time / 60

    result = hours
    return result

print(solution())