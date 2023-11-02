def solution():
    """Gina chooses what she and her sister will watch on Netflix three times as often as her sister does. If her sister watches a total of 24 shows on Netflix per week, and each show is 50 minutes long, how many minutes of Netflix does Gina get to choose?"""
    # Define the ratio of how often Gina chooses to how often her sister chooses
    RATIO = 3

    # Define the number of shows Gina's sister watches per week
    sister_shows = 24

    # Calculate the total number of shows watched per week
    total_shows = 4 * sister_shows

    # Calculate the number of times Gina chooses what to watch
    gina_choices = RATIO * sister_shows

    # Calculate the total number of minutes of Netflix that Gina chooses
    gina_minutes = gina_choices * 50

    # Display the total number of minutes that Gina chooses
    result = gina_minutes
    return result

print(solution())