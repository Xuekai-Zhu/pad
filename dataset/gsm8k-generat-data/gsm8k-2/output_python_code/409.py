def solution():
    """Mark wants to set the record for most consecutive ropes jumped. The record is 54,000. He can jump 3 times a second. How many hours would he need to jump rope?"""
    record = 54000
    jumps_per_second = 3
    total_jumps = record / jumps_per_second
    total_seconds = total_jumps / jumps_per_second
    total_hours = total_seconds / 3600
    result = total_hours
    return result

print(solution())