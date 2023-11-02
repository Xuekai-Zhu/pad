def solution():
    """The Llesis family drove and hiked 6 hours to their vacation spot. They drove an average of 50 miles per hour and hiked an average of 5 miles per hour less than half their speed when they drive. If it took them 1.5 hours to hike, how far was their vacation spot?"""
    drive_speed = 50
    hike_speed = (drive_speed / 2) - 5
    hike_time = 1.5
    drive_time = 6 - hike_time
    total_distance = (drive_speed * drive_time) + (hike_speed * hike_time)
    result = total_distance
    return result

print(solution())