def solution():
    great_gatsby_pages = 218
    the_raven_pages = 42
    reading_speed = 2 # pages per minute
    time_to_read_gatsby = great_gatsby_pages / reading_speed
    time_to_read_raven = the_raven_pages / reading_speed
    if time_to_read_gatsby < time_to_read_raven:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())