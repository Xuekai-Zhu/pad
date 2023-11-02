def solution():
    """Rosie runs 6 miles per hour. She runs for 1 hour on Monday, 30 minutes on Tuesday, 1 hour on Wednesday, and 20 minutes on Thursday. If she wants to run 20 miles for the week, how many minutes should she run on Friday?"""
    # Define Rosie's running speed and the time she runs for on Monday, Tuesday, Wednesday, and Thursday
    speed = 6
    monday_time = 1
    tuesday_time = 0.5
    wednesday_time = 1
    thursday_time = 0.2

    # Calculate the total distance Rosie runs in the first four days
    total_distance = (monday_time + tuesday_time + wednesday_time + thursday_time) * speed

    # Calculate the remaining distance Rosie needs to run for the week
    remaining_distance = 20 - total_distance

    # Calculate the time Rosie needs to run at her speed to cover the remaining distance
    friday_time = remaining_distance / speed * 60

    # return the result
    result = round(friday_time)
    return result

print(solution())