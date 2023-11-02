def solution():
    """Mark wants to set the record for most consecutive ropes jumped. The record is 54,000. He can jump 3 times a second. How many hours would he need to jump rope?"""
    total_jumps = 54000
    jumps_per_second = 3
    seconds_per_hour = 3600
    total_hours = total_jumps / jumps_per_second / seconds_per_hour
    result = total_hours
    return result

print(solution())