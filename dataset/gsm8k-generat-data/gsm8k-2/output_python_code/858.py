def solution():
    """The gummy bear factory manufactures 300 gummy bears a minute. Each packet of gummy bears has 50 gummy bears inside. How long would it take for the factory to manufacture enough gummy bears to fill 240 packets, in minutes?"""
    gummy_bears_per_minute = 300
    gummy_bears_per_packet = 50
    total_gummy_bears = gummy_bears_per_packet * 240
    time_in_minutes = total_gummy_bears / gummy_bears_per_minute
    result = time_in_minutes
    return result

print(solution())