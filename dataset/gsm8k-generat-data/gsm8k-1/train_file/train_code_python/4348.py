def solution():
    """This evening in the nighttime sky over Texas, Mars can be seen until 12:10 AM. Jupiter does not appear until 2 hours and 41 minutes later, and Uranus does not appear until 3 hours and 16 minutes after Jupiter makes its first appearance. How many minutes after 6:00 AM does Uranus first appear in the evening sky over Texas this evening?"""
    mars_disappears = 1210
    jupiter_appears = mars_disappears + 2 * 60 + 41
    uranus_appears = jupiter_appears + 3 * 60 + 16
    time_difference = uranus_appears - 6 * 60
    result = time_difference
    return result

print(solution())