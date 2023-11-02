def solution():
    
    gummy_bears_per_minute = 300
    gummy_bears_per_packet = 50
    total_gummy_bears = gummy_bears_per_packet * 240
    time_in_minutes = total_gummy_bears / gummy_bears_per_minute
    result = time_in_minutes
    return result

print(solution())