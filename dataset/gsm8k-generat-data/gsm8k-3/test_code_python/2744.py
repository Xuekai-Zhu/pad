def solution():
    """Ben's potato gun can launch a potato 6 football fields. If a football field is 200 yards long and Ben's dog can run 400 feet/minute, how many minutes will it take his dog to fetch a potato he launches?"""
    # Define the distance the potato is launched in yards
    LAUNCH_DISTANCE = 6 * 200

    # Convert the launch distance to feet
    launch_distance_feet = LAUNCH_DISTANCE * 3

    # Calculate the time it will take the dog to run to the potato in minutes
    time_to_fetch = launch_distance_feet / 400

    result = time_to_fetch
    return result

print(solution())