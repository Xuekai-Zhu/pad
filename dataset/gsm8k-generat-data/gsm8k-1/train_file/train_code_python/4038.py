def solution():
    """Jenna is planning a road trip. She plans on driving the first 200 miles, and her friend will drive the last 100 miles. They plan on taking 2 30-minute breaks. If Jenna drives 50 miles per hour and her friend drives 20 miles per hour, how many hours will they spend on the road trip?"""
    jenna_distance = 200
    friend_distance = 100
    jenna_speed = 50
    friend_speed = 20
    total_distance = jenna_distance + friend_distance
    time_driving = (jenna_distance / jenna_speed) + (friend_distance / friend_speed)
    time_breaks = 2 * 0.5 # Two 30-minute breaks
    total_time = time_driving + time_breaks
    result = total_time
    return result

print(solution())