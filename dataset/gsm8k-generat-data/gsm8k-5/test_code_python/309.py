def solution():
    typing_speed = 50  # Carl types at a speed of 50 words per minute
    minutes_per_hour = 60  # There are 60 minutes in an hour
    hours_per_day = 4  # Carl types for 4 hours per day
    days = 7  # Carl wants to know how many words he can type in 7 days

    # Calculate the total number of minutes Carl types in 7 days
    total_minutes = minutes_per_hour * hours_per_day * days

    # Calculate the total number of words Carl can type in 7 days
    total_words = typing_speed * total_minutes
    result = total_words
    return result

print(solution())