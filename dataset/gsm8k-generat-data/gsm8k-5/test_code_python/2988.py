def solution():
    paintings_per_hour = 12 / 6  # Hadassah paints 2 paintings per hour
    total_paintings = 12 + 20  # Hadassah needs to paint a total of 32 paintings

    # Calculate the total time Hadassah will take to finish all the paintings
    total_time = total_paintings / paintings_per_hour
    result = total_time
    return result

print(solution())