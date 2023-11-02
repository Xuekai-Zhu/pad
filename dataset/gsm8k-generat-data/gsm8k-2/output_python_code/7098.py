def solution():
    """Matt skips ropes 3 times per second. If he jumped for 10 minutes how many skips hops did he get?"""
    skips_per_second = 3
    jumps_per_minute = skips_per_second * 60
    duration_in_minutes = 10
    total_jumps = jumps_per_minute * duration_in_minutes
    result = total_jumps
    return result

print(solution())