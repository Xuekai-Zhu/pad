def solution():
    """Two runners are competing in a 10-mile race.  The first runs at an average pace of 8 minutes per mile, while the second runs at an average pace of 7 minutes per mile.  After 56 minutes, the second runner stops for a drink of water.  For how many minutes could the second runner remain stopped before the first runner catches up with him?"""
    # Define the distance of the race
    distance = 10

    # Define the average pace of the first and second runners
    pace_runner1 = 8 # minutes per mile
    pace_runner2 = 7 # minutes per mile

    # Calculate the time taken by the first runner to complete the race
    # time = distance * pace
    time_runner1 = distance * pace_runner1 # minutes

    # Calculate the distance covered by the second runner before taking a break
    distance_runner2 = (56 / 60) * pace_runner2 * distance

    # Calculate the time taken by the second runner to cover that distance
    time_runner2_before_break = 56 + (distance_runner2 / pace_runner2)

    # Calculate the remaining distance to complete the race
    remaining_distance = distance - (distance_runner2 / distance)

    # Calculate the time taken by the first runner to complete the remaining distance
    time_runner1_for_remaining_distance = remaining_distance * pace_runner1

    # Calculate the total time taken by the first runner to complete the race
    # time = time before break + time for remaining distance
    time_runner1_total = time_runner2_before_break + time_runner1_for_remaining_distance

    # Calculate the time that the second runner can remain stopped before being caught up by the first runner
    time_remaining_for_runner2 = time_runner1_total - (56 + (distance_runner2 / pace_runner2))

    result = time_remaining_for_runner2
    return result

print(solution())