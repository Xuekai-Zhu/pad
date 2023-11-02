def solution():
    words_per_minute = 50
    words_per_page = 400
    num_pages = 5
    water_per_hour = 15

    # Calculate the total number of words in the entire paper
    total_words = words_per_page * num_pages

    # Calculate the total time it will take Stan to type the paper in minutes
    total_time_in_minutes = total_words / words_per_minute

    # Calculate the total amount of water Stan needs to drink
    total_water = (total_time_in_minutes / 60) * water_per_hour
    result = total_water
    return result

print(solution())