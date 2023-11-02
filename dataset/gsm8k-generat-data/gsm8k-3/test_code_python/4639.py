def solution():
    """John scores 2 shots worth 2 points and 1 shot worth 3 points every 4 minutes.  He plays for 2 periods.  Each period is 12 minutes.  How many points does he score?"""
    # Define the number of points per shot
    TWO_POINT_SHOT = 2
    THREE_POINT_SHOT = 3

    # Define the number of shots John scores per 4-minute block
    two_point_shots = 2
    three_point_shots = 1

    # Calculate the number of blocks John plays during 2 periods
    num_blocks = 2 * 12 // 4

    # Calculate the total number of points John scores
    total_points = num_blocks * (two_point_shots*TWO_POINT_SHOT + three_point_shots*THREE_POINT_SHOT)

    # Display the total number of points
    result = total_points
    return result

print(solution())