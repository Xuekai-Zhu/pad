def solution():
    gummy_bears_per_minute = 300
    gummy_bears_per_packet = 50
    packets_needed = 240
    minutes_needed = packets_needed * gummy_bears_per_packet / gummy_bears_per_minute
    result = minutes_needed
    return result

print(solution())