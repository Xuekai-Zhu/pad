def solution():
    """The gummy bear factory manufactures 300 gummy bears a minute. Each packet of gummy bears has 50 gummy bears inside. How long would it take for the factory to manufacture enough gummy bears to fill 240 packets, in minutes?"""
    # Define the number of gummy bears produced per minute and the number of gummy bears per packet
    gummy_bears_per_minute = 300
    gummy_bears_per_packet = 50

    # Calculate the total number of gummy bears needed to fill 240 packets
    total_gummy_bears_needed = gummy_bears_per_packet * 240

    # Calculate the amount of time in minutes needed to produce enough gummy bears
    minutes_needed = total_gummy_bears_needed / gummy_bears_per_minute

    # Return the result
    result = minutes_needed
    return result

print(solution())