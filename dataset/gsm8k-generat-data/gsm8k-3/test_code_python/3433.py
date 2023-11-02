def solution():
    """Two runners are competing in a 10-mile race.  The first runs at an average pace of 8 minutes per mile, while the second runs at an average pace of 7 minutes per mile.  After 56 minutes, the second runner stops for a drink of water.  For how many minutes could the second runner remain stopped before the first runner catches up with him?"""

    # Define the distance of the race
    distance = 10

    # Define the pace of each runner
    pace_runner1 = 8 # minutes per mile
    pace_runner2 = 7 # minutes per mile

    # Calculate the time it takes for each runner to complete the race
    time_runner1 = distance * pace_runner1 # minutes
    time_runner2 = distance * pace_runner2 # minutes

    # Subtract the time the second runner spends on the drink stop from their total time
    time_runner2 -= 56 # minutes

    # Calculate how long the second runner could remain stopped and still be caught by the first runner
    catch_time = (time_runner2 - time_runner1) / (pace_runner1 - pace_runner2) # minutes

    # Display the catch time
    result = catch_time
    return result

print(solution())