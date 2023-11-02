def solution():
    # Define the ratio of Gina's choices to her sister's choices
    gina_to_sister_ratio = 3/1

    # Calculate the total number of shows watched per week
    total_shows = 24

    # Calculate the number of shows Gina chooses
    gina_shows = gina_to_sister_ratio / 4 * total_shows

    # Convert the number of shows to minutes
    gina_minutes = gina_shows * 50
    result = gina_minutes
    return result

print(solution())