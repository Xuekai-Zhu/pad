def solution():
    segments_eaten = 60 + 2*2*60  # The scorpion has already eaten one millipede with 60 segments and 2 that are twice as long
    segments_remaining = 800 - segments_eaten  # Calculate how many segments are left to eat
    millipedes_needed = segments_remaining / 50  # Divide remaining segments by the number of segments in a 50-segment millipede
    result = millipedes_needed
    return result

print(solution())