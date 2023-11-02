def solution():
    """Laura is planning her wedding. She expects 220 people to attend the wedding, but she has been told that approximately 5% typically don't show. How many people will go to her wedding?"""
    # Define the expected number of attendees and the percentage of no-shows
    expected_attendees = 220
    no_show_percentage = 0.05

    # Calculate the number of people who won't show up
    no_shows = expected_attendees * no_show_percentage

    # Calculate the number of people who will actually show up
    actual_attendees = expected_attendees - no_shows

    # Return the result
    result = actual_attendees
    return result

print(solution())