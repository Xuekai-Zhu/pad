def solution():
    num_suggestions = 15
    num_tries = 5
    final_choice = 5

    # Calculate the total number of videos that Billy watches before finding the one he likes
    total_watched = num_suggestions * num_tries

    # Add the final video that Billy watches
    total_watched += final_choice

    result = total_watched
    return result

print(solution())