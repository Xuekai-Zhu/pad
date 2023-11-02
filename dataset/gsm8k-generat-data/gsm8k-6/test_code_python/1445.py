def solution():
    # Calculate the total number of words in all the books
    total_words = 200 + 400 + 300

    # Calculate the total number of hours required to complete all the books
    total_hours = total_words / 100

    # Calculate the average number of minutes to spend reading per day
    avg_minutes_per_day = (total_hours * 60) / 10
    result = avg_minutes_per_day
    return result

print(solution())