def solution():
    """Dave breaks 2 guitar strings per night when playing live. If he performs 6 shows a week for 12 weeks, how many guitar strings will he need to replace?"""
    # Define the number of guitar strings broken per show
    strings_per_show = 2

    # Calculate the total number of shows
    total_shows = 6 * 12

    # Calculate the total number of guitar strings broken
    total_strings = strings_per_show * total_shows

    # return the result
    result = total_strings
    return result

print(solution())