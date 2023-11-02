def solution():
    """Jenna is planning a road trip. She plans on driving the first 200 miles, and her friend will drive the last 100 miles. They plan on taking 2 30-minute breaks. If Jenna drives 50 miles per hour and her friend drives 20 miles per hour, how many hours will they spend on the road trip?"""
    jenna_distance = 200
    friend_distance = 100
    jenna_speed = 50
    friend_speed = 20
    break_time = 2 * 0.5  # 2 breaks of 30 minutes each
    jenna_drive_time = jenna_distance / jenna_speed
    friend_drive_time = friend_distance / friend_speed
    total_time = jenna_drive_time + friend_drive_time + break_time
    result = total_time
    return result

print(solution())