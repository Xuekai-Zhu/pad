def solution():
    # Calculate the time it takes Hadassah to paint one painting
    time_per_painting = 6 / 12

    # Calculate the time it takes Hadassah to paint the additional 20 paintings
    additional_paintings_time = 20 * time_per_painting

    # Calculate the total time it takes Hadassah to finish all the paintings
    total_time = 6 + additional_paintings_time
    result = total_time
    return result

print(solution())