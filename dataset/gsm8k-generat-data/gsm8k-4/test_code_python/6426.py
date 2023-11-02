def solution():
    """A blind cave scorpion survives by catching millipedes. It needs to eat lots of millipedes to survive: a total of 800 body segments every day. If it's already eaten one millipede with 60 segments and 2 millipedes that are twice as long, how many 50-segment millipedes does it need to eat to reach its daily total?"""
    # Define the total number of body segments needed
    total_segments_needed = 800

    # Determine the number of segments eaten from the first millipede
    segments_eaten = 60

    # Determine the number of segments eaten from the two larger millipedes
    segments_eaten += 2 * 2 * 60

    # Determine the remaining number of segments needed
    segments_remaining = total_segments_needed - segments_eaten

    # Calculate the number of 50-segment millipedes needed to reach the remaining number of segments
    millipedes_needed = segments_remaining / 50

    # Round up to the nearest whole number of millipedes
    millipedes_needed = math.ceil(millipedes_needed)

    # Return the result
    result = millipedes_needed
    return result

print(solution())