def solution():
    """Gina chooses what she and her sister will watch on Netflix three times as often as her sister does. If her sister watches a total of 24 shows on Netflix per week, and each show is 50 minutes long, how many minutes of Netflix does Gina get to choose?"""
    # Define the number of shows watched by the sister
    sister_shows = 24

    # Define the ratio of shows watched by Gina and her sister
    ratio = 3 / 1

    # Calculate the total number of shows watched by both
    total_shows = sister_shows * (1 + ratio)

    # Calculate the number of shows chosen by Gina
    gina_shows = sister_shows * ratio

    # Calculate the total number of minutes of Netflix watched
    total_minutes = total_shows * 50

    # Calculate the number of minutes of Netflix chosen by Gina
    gina_minutes = gina_shows * 50

    # return the result
    result = gina_minutes
    return result

print(solution())