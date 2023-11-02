def solution():
    """The gummy bear factory manufactures 300 gummy bears a minute. Each packet of gummy bears has 50 gummy bears inside. How long would it take for the factory to manufacture enough gummy bears to fill 240 packets, in minutes?"""
    # Define the number of gummy bears per packet
    BEARS_PER_PACKET = 50

    # Define the number of packets to fill
    packets = 240

    # Calculate the total number of gummy bears needed
    total_bears = packets * BEARS_PER_PACKET

    # Calculate the time needed to manufacture the gummy bears
    time = total_bears / 300

    # Display the time needed in minutes
    result = time
    return result

print(solution())