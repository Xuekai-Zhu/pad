def solution():
    # Calculate the total number of seconds
    total_seconds = 130 + 145 + 85 + 60 + 180

    # Convert seconds to minutes
    total_minutes = total_seconds / 60

    # Calculate the average minutes for each player
    avg_minutes = total_minutes / 5
    result = avg_minutes
    return result

print(solution())