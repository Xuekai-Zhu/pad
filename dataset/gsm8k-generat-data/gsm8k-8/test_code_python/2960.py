def solution():
    # Define the typing speed and number of words to type
    typing_speed = 60  # words per minute
    words_to_type = 10800

    # Calculate the number of minutes Emily will take to type the words
    minutes_to_type = words_to_type / typing_speed

    # Convert minutes to hours
    hours_to_type = minutes_to_type / 60
    result = hours_to_type
    return result

print(solution())