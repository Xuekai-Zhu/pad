def solution():
    """This evening in the nighttime sky over Texas, Mars can be seen until 12:10 AM. Jupiter does not appear until 2 hours and 41 minutes later, and Uranus does not appear until 3 hours and 16 minutes after Jupiter makes its first appearance. How many minutes after 6:00 AM does Uranus first appear in the evening sky over Texas this evening?"""
    mars_end_time = datetime.datetime.strptime("12:10 AM", "%I:%M %p")
    jupiter_start_time = mars_end_time + datetime.timedelta(hours=2, minutes=41)
    uranus_start_time = jupiter_start_time + datetime.timedelta(hours=3, minutes=16)
    start_time = datetime.datetime.strptime("6:00 AM", "%I:%M %p")
    time_difference = uranus_start_time - start_time
    result = time_difference.total_seconds() // 60
    return result

print(solution())