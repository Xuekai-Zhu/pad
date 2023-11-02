def solution():
    speed = 50  # words per minute
    hours_per_day = 4
    days = 7

    # Calculate the total number of minutes Carl types in 7 days
    total_minutes = hours_per_day * 60 * days

    # Calculate the total number of words Carl can type in 7 days
    total_words = speed * total_minutes
    result = total_words
    return result

print(solution())