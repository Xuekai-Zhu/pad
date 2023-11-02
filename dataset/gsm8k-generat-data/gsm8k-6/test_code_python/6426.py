def solution():
    # Calculate the total number of segments already eaten by the scorpion
    eaten_segments = 60 + 2 * (2 * 60)  # one millipede with 60 segments and 2 millipedes that are twice as long

    # Calculate the remaining segments the scorpion needs to eat
    remaining_segments = 800 - eaten_segments

    # Calculate the number of 50-segment millipedes the scorpion needs to eat to reach its daily total
    num_50_segment_millipedes = remaining_segments / 50

    result = num_50_segment_millipedes
    return result

print(solution())