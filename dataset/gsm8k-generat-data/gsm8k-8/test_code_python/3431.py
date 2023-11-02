def solution():
    # Calculate the total distance the winner ran
    total_distance = 24 * 100

    # Calculate the amount they earned for that distance
    earned = total_distance / 100 * 3.5

    # Calculate their earning per minute
    earning_per_minute = earned / 12
    result = earning_per_minute
    return result

print(solution())