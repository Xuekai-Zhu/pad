def solution():
    # Define the number of words Jaydee can type in a minute and the total number of words in the research paper
    words_per_minute = 38
    total_words = 4560

    # Calculate the number of minutes it will take to type the research paper
    minutes_to_type = total_words / words_per_minute

    # Convert the minutes to hours
    hours_to_type = minutes_to_type / 60
    result = hours_to_type
    return result

print(solution())