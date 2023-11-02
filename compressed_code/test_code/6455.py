def solution():
    
    gummy_bears_per_minute = 300
    gummy_bears_per_packet = 50
    packets_needed = 240
    total_gummy_bears_needed = packets_needed * gummy_bears_per_packet
    time_in_minutes = total_gummy_bears_needed / gummy_bears_per_minute
    result = time_in_minutes
    return result

print(solution())