def solution():
    # Calculate the total number of shots and points scored by John in 2 periods
    total_shots = 2 * 2 + 1 * 2  # John scores 2 shots worth 2 points and 1 shot worth 3 points every 4 minutes
    total_shots *= 2 * 12  # John plays for 2 periods of 12 minutes each
    total_points = total_shots // 2 * 2 + total_shots % 2 * 3  # each shot worth 2 points or 3 points
    result = total_points
    return result

print(solution())