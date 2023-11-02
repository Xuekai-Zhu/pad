def solution():
    typing_speed = 50  # Stan types 50 words per minute
    words_per_page = 400  # Each page contains 400 words
    pages = 5  # Stan needs to write a 5-page paper

    # Calculate the total number of words Stan needs to type
    total_words = words_per_page * pages

    # Calculate the total time Stan will spend typing in minutes
    total_time = total_words / typing_speed

    # Calculate the total amount of water Stan needs to drink in ounces
    water_per_hour = 15  # Stan needs to drink 15 ounces of water per hour
    total_water = (total_time / 60) * water_per_hour

    result = total_water
    return result

print(solution())