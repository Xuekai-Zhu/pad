def solution():
    gummy_bears_per_minute = 300
    gummy_bears_per_packet = 50
    num_packets = 240

    # Calculate the total number of gummy bears needed to fill all the packets
    total_gummy_bears = num_packets * gummy_bears_per_packet

    # Calculate the number of minutes it will take to manufacture all the gummy bears
    time_in_minutes = total_gummy_bears / gummy_bears_per_minute
    result = time_in_minutes
    return result

print(solution())