def solution():
    """Jake decides to go to the beach for a fun day. It is a 2-hour drive each way. He then spends 2.5 times at long at the beach as his total driving time. How much time does the trip take?"""
    drive_time = 2 * 2 # 2 hours each way
    beach_time = drive_time * 2.5 # 2.5 times as long as drive time
    total_time = drive_time + beach_time
    result = total_time
    return result

print(solution())