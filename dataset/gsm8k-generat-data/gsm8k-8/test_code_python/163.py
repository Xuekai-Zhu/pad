def solution():
    # Calculate the total points scored from touchdowns
    touchdown_points = 4 * 6 * 15

    # Calculate the total points scored from 2 point conversions
    conversion_points = 2 * 6

    # Calculate the total points scored in the season
    total_points = touchdown_points + conversion_points

    # Calculate the amount James beat the old record by
    old_record = 300
    points_above_record = total_points - old_record
    result = points_above_record
    return result

print(solution())