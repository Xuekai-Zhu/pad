def solution():
    # Calculate the total number of words in the paper
    total_words = 5 * 400  # each page contains 400 words and there are 5 pages in the paper

    # Calculate the time required to type the paper in minutes
    typing_time = total_words / 50  # Stan can type 50 words per minute

    # Calculate the number of hours needed to type the paper
    typing_hours = typing_time / 60

    # Calculate the amount of water Stan needs to drink while typing
    water_needed = typing_hours * 15  # Stan needs to drink 15 ounces of water per hour of typing

    result = water_needed
    return result

print(solution())