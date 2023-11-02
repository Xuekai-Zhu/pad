def solution():
    # Calculate the average distance jumped for each athlete
    avg_athlete1 = (26 + 30 + 7) / 3  
    avg_athlete2 = (24 + 34 + 8) / 3 

    # Determine which athlete had the higher average jump
    if avg_athlete1 > avg_athlete2:
        winner_avg = avg_athlete1
    else:
        winner_avg = avg_athlete2

    result = winner_avg
    return result

print(solution())