def solution():
    """Gunther can type 160 words every 3 minutes and he works 480 minutes per day. How many words can Gunther type in a working day?"""
    # Define Gunther's typing speed and work hours per day
    typing_speed = 160 / 3  # words per minute
    work_hours = 480 / 60  # hours

    # Calculate the total number of words Gunther can type in a day
    total_words = typing_speed * work_hours * 60

    # return the result
    result = total_words
    return result

print(solution())