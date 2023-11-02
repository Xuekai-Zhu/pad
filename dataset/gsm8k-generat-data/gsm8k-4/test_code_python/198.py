def solution():
    """Rosie runs 6 miles per hour. She runs for 1 hour on Monday, 30 minutes on Tuesday, 1 hour on Wednesday, and 20 minutes on Thursday. If she wants to run 20 miles for the week, how many minutes should she run on Friday?"""
    # Define the total distance and time already run
    total_distance = 0
    total_time = 0

    # Calculate the distance and time run on each day
    monday_distance = 6 * 1
    monday_time = 60
    total_distance += monday_distance
    total_time += monday_time

    tuesday_distance = 6 * 0.5
    tuesday_time = 30
    total_distance += tuesday_distance
    total_time += tuesday_time

    wednesday_distance = 6 * 1
    wednesday_time = 60
    total_distance += wednesday_distance
    total_time += wednesday_time

    thursday_distance = 6 * 0.33
    thursday_time = 20
    total_distance += thursday_distance
    total_time += thursday_time

    # Calculate the remaining distance to run on Friday
    remaining_distance = 20 - total_distance

    # Calculate how long Rosie needs to run on Friday to cover the remaining distance
    friday_time = (remaining_distance / 6) * 60

    result = friday_time
    return result

print(solution())