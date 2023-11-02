def solution():
    sister_shows = 24
    gina_shows = 3 * sister_shows

    show_length = 50  # measured in minutes

    # Calculate the total number of minutes of Netflix that Gina gets to choose
    gina_minutes = gina_shows * show_length

    result = gina_minutes
    return result

print(solution())