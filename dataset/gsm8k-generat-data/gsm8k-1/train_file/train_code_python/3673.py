def solution():
    """At a UFO convention, there are 120 conference attendees. If there are 4 more male attendees than female attendees, how many male attendees are there?"""
    total_attendees = 120
    # Let x be the number of female attendees
    # Then the number of male attendees is x + 4
    x = (total_attendees - 4) / 2
    result = x + 4
    return result

print(solution())