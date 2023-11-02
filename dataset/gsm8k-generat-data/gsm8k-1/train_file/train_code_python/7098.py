def solution():
    """Matt skips ropes 3 times per second. If he jumped for 10 minutes how many skips hops did he get?"""
    seconds_per_minute = 60
    jumps_per_second = 3
    total_seconds = 10 * seconds_per_minute
    total_jumps = jumps_per_second * total_seconds
    result = total_jumps
    return result

print(solution())