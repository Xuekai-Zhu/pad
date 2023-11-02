def solution():
    """This evening in the nighttime sky over Texas, Mars can be seen until 12:10 AM. Jupiter does not appear until 2 hours and 41 minutes later, and Uranus does not appear until 3 hours and 16 minutes after Jupiter makes its first appearance.  How many minutes after 6:00 AM does Uranus first appear in the evening sky over Texas this evening?"""
    
    # Calculate the time in minutes at which Mars disappears
    mars_disappear = 12 * 60 + 10

    # Calculate the time in minutes at which Jupiter appears
    jupiter_appear = mars_disappear + 2 * 60 + 41

    # Calculate the time in minutes at which Uranus appears
    uranus_appear = jupiter_appear + 3 * 60 + 16

    # Calculate the time in minutes elapsed since 6:00 AM until Uranus appears
    elapsed_time = uranus_appear - 6 * 60

    # Display the elapsed time in minutes
    result = elapsed_time
    return result

print(solution())