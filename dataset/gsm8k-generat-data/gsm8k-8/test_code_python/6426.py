def solution():
    # Calculate the total number of segments eaten so far
    segments_eaten = 1*60 + 2*(2*60)

    # Calculate the remaining number of segments needed
    segments_remaining = 800 - segments_eaten

    # Calculate the number of 50-segment millipedes needed to reach the daily total
    millipedes_needed = segments_remaining / 50
    result = millipedes_needed
    return result

print(solution())