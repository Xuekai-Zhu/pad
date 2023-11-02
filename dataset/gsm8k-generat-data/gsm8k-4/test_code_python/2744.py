def solution():
    """Ben's potato gun can launch a potato 6 football fields. If a football field is 200 yards long and Ben's dog can run 400 feet/minute, how many minutes will it take his dog to fetch a potato he launches?"""
    # Define the distance the potato is launched in yards
    potato_distance = 6 * 200 * 3

    # Convert the distance to feet
    potato_distance_feet = potato_distance * 3

    # Calculate the time it takes the dog to run to the potato in minutes
    time = potato_distance_feet / 400 / 60

    # Round the time to the nearest minute
    result = round(time)
    return result

print(solution())