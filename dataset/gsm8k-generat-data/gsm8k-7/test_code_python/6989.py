def solution():
    weekly_hours = 30
    time_per_painting = 3
    num_weeks = 4

    # Calculate the total number of hours the artist has to paint in 4 weeks
    total_hours = weekly_hours * num_weeks

    # Calculate the total number of paintings the artist can complete in 4 weeks
    num_paintings = total_hours / time_per_painting
    result = num_paintings
    return result

print(solution())