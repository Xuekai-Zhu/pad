def solution():
    # Define how many pages Juwella read 2 nights ago and last night
    pages_two_nights_ago = 15 * 2
    pages_last_night = pages_two_nights_ago + 5

    # Calculate how many pages are left to read
    pages_left_to_read = 100 - (15 + pages_two_nights_ago + pages_last_night)

    result = pages_left_to_read
    return result

print(solution())