def solution():
    """Laura is planning her wedding. She expects 220 people to attend the wedding, but she has been told that approximately 5% typically don't show. How many people will go to her wedding?"""
    # Define the expected number of attendees and the percentage that typically don't show
    expected_attendees = 220
    percent_not_attending = 0.05

    # Calculate the number of people who typically don't show
    num_not_attending = expected_attendees * percent_not_attending

    # Calculate the number of people who will attend the wedding
    num_attending = expected_attendees - num_not_attending

    # Display the number of people who will attend the wedding
    result = num_attending
    return result

print(solution())