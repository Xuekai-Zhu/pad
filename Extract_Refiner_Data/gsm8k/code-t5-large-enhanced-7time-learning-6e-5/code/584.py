def solution():
    
    # Define the initial typing speed and the additional words
    initial_speed = 47
    additional_words = 5

    # Calculate the total number of words after the first increase
    total_words = initial_speed + additional_words

    # Calculate the total time taken to increase the speed
    total_time = initial_speed + additional_words

    # Calculate the average of the three measurements
    average_speed = total_words / total_time

    # Display the average of the three measurements
    result = average_speed
    return result

print(solution())