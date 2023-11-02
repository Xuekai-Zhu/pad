def solution():
    """At a UFO convention, there are 120 conference attendees. If there are 4 more male attendees than female attendees, how many male attendees are there?"""
    # Define the total number of attendees
    total_attendees = 120

    # Let x be the number of female attendees
    x = (total_attendees - 4) / 2

    # Calculate the number of male attendees
    male_attendees = x + 4

    # Display the number of male attendees
    result = male_attendees
    return result

print(solution())