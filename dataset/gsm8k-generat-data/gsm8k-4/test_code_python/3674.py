def solution():
    """At a UFO convention, there are 120 conference attendees. If there are 4 more male attendees than female attendees, how many male attendees are there?"""
    # Define the total number of attendees
    total_attendees = 120

    # Calculate the number of female attendees
    female_attendees = (total_attendees - 4) / 2

    # Calculate the number of male attendees
    male_attendees = female_attendees + 4

    # Return the number of male attendees
    result = male_attendees
    return result

print(solution())