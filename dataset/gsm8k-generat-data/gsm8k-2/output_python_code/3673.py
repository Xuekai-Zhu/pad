def solution():
    """At a UFO convention, there are 120 conference attendees. If there are 4 more male attendees than female attendees, how many male attendees are there?"""
    total_attendees = 120
    # Let's assume x is the number of female attendees
    x = (total_attendees - 4) / 2
    # The number of male attendees is 4 more than the number of female attendees
    male_attendees = x + 4
    result = male_attendees
    return result

print(solution())