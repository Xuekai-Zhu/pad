def solution():
    """This evening in the nighttime sky over Texas, Mars can be seen until 12:10 AM. Jupiter does not appear until 2 hours and 41 minutes 
    later, and Uranus does not appear until 3 hours and 16 minutes after Jupiter makes its first appearance. How many minutes after 6:00 AM 
    does Uranus first appear in the evening sky over Texas this evening?"""
    # Define the time when Mars disappears and the time when Jupiter appears
    mars_disappear = 12 * 60 + 10  # in minutes
    jupiter_appear = mars_disappear + 2 * 60 + 41  # in minutes

    # Define the time when Uranus appears
    uranus_appear = jupiter_appear + 3 * 60 + 16  # in minutes

    # Define the time when Uranus first appears after 6:00 AM
    time_after_six_am = uranus_appear - 6 * 60  # in minutes

    result = time_after_six_am
    return result

print(solution())