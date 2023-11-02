def solution():
    """A blind cave scorpion survives by catching millipedes. It needs to eat lots of millipedes to survive: a total of 800 body segments every day. If it's already eaten one millipede with 60 segments and 2 millipedes that are twice as long, how many 50-segment millipedes does it need to eat to reach its daily total?"""
    # Define the number of segments in each type of millipede
    MILLIPEDE_1_SEGMENTS = 60
    MILLIPEDE_2_SEGMENTS = 2 * MILLIPEDE_1_SEGMENTS
    MILLIPEDE_3_SEGMENTS = 50

    # Define the number of millipedes of each type that have already been eaten
    millipede_1 = 1
    millipede_2 = 2

    # Calculate the total number of segments already eaten
    total_segments_eaten = (millipede_1 * MILLIPEDE_1_SEGMENTS) + (millipede_2 * MILLIPEDE_2_SEGMENTS)

    # Calculate the number of segments still needed
    segments_needed = 800 - total_segments_eaten

    # Calculate the number of 50-segment millipedes needed to reach the daily total
    millipede_3_needed = segments_needed // MILLIPEDE_3_SEGMENTS

    # Display the number of millipedes needed
    result = millipede_3_needed
    return result

print(solution())