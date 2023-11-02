def solution():
    """Jaydee can type 38 words in a minute. How many hours will he take to finish typing a research paper with 4560 words?"""
    # Define the number of words Jaydee can type in a minute and the total number of words in the research paper
    words_per_minute = 38
    total_words = 4560

    # Calculate the total number of minutes it will take to type the research paper
    total_minutes = total_words / words_per_minute

    # Convert the total minutes to hours
    total_hours = total_minutes / 60

    # Return the result rounded to 2 decimal places
    result = round(total_hours, 2)
    return result

print(solution())