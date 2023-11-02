def solution():
    """Theon's ship can move 15 nautical miles per hour while Yara's ship can move 30 nautical miles per hour. If their destination is 90 nautical miles away, how many hours ahead will Yara be ahead of Theon?"""
    distance = 90
    theon_speed = 15
    yara_speed = 30
    theon_time = distance / theon_speed
    yara_time = distance / yara_speed
    time_difference = yara_time - theon_time
    result = time_difference
    return result

print(solution())