def solution():
    # Calculate the total number of gummy bears needed to fill 240 packets
    total_gummy_bears = 240 * 50  # each packet has 50 gummy bears

    # Calculate the time taken to manufacture the total number of gummy bears
    time_taken = total_gummy_bears / 300  # the factory manufactures 300 gummy bears a minute

    result = time_taken
    return result

print(solution())