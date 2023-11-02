def solution():
    gummy_bears_per_minute = 300  # The factory manufactures 300 gummy bears per minute
    gummy_bears_per_packet = 50  # Each packet has 50 gummy bears

    # Calculate the total number of gummy bears needed to fill 240 packets
    total_gummy_bears = gummy_bears_per_packet * 240

    # Calculate how long it will take to manufacture the required number of gummy bears
    time_in_minutes = total_gummy_bears / gummy_bears_per_minute
    result = time_in_minutes
    return result

print(solution())